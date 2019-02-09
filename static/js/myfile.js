function promotions(listProducts){
    let priceLettuce = parseFloat($('#qtd_input_1').val())
    let priceBacon = parseFloat($('#qtd_input_2').val())
    let priceBurger = parseFloat($('#qtd_input_3').val())
    let priceEgg = parseFloat($('#qtd_input_4').val())
    let priceCheese = parseFloat($('#qtd_input_5').val())
    let total = 0;
    let desc = 0;
    total = (listProducts[0] * priceLettuce) + (listProducts[1] * priceBacon) + (listProducts[2] * priceBurger) + (listProducts[3] *priceEgg) + (listProducts[4] * priceCheese);
    totalNoDesc = total;
    if(listProducts[1] >= 3 || listProducts[2] >= 3 ){
        let qtdLessIngredientBacon = Math.floor(listProducts[1]/3);
        let qtdLessIngredienthamburguer = Math.floor(listProducts[2]/3);
        qtdLessIngredientBacon =  qtdLessIngredientBacon * priceBacon;
        qtdLessIngredienthamburguer = qtdLessIngredienthamburguer * priceBurger;
        total -= qtdLessIngredientBacon;
        total -= qtdLessIngredienthamburguer;
        desc += qtdLessIngredientBacon + qtdLessIngredienthamburguer;
    }
    if(listProducts[4] >= 3){
        let qtdLessIngredientCheese = Math.floor(listProducts[4]/3);
        qtdLessIngredientCheese = qtdLessIngredientCheese * priceCheese;
        total -= qtdLessIngredientCheese;
        desc += qtdLessIngredientCheese;
    }
    if(listProducts[0] > 0 && listProducts[1] == 0){
        desc += (total * 0.1 );
        total =   total - (total * 0.1 );  
    }
    let responseValues = {'total':total, 'totalNoDesc': totalNoDesc, 'Desc': desc };
    return responseValues
}


function productValue(){
    let qtdLettuce = parseInt($('#input_0').val());
    let qtdBacon = parseInt($('#input_1').val());
    let qtdBurger = parseInt($('#input_2').val());
    let qtdEgg = parseInt($('#input_3').val());
    let qtdCheese = parseInt($('#input_4').val());
    let listProducts = [qtdLettuce, qtdBacon, qtdBurger, qtdEgg, qtdCheese]
    let responseValues = promotions(listProducts)
    $('#value').text("Valor a pagar R$: " + responseValues['total'].toFixed(2).toString());
    $('#valueTNoDesc').text("Valor total sem descontos R$: "+ responseValues['totalNoDesc'].toFixed(2).toString());
    $('#valueDesc').text("Valor do desconto R$: "+responseValues['Desc'].toFixed(2).toString());
}
function inputValues(input, type){
    let inputValue = parseInt($('#'+input).val());
    if(type==0){
        if(inputValue != 0){
            $('#'+input).val(inputValue-1);
            productValue();
        }
    }else{
        $('#'+input).val(inputValue+1);
        productValue();
    }
}


function hasValue(currentValue){
    return currentValue == 0 
}

setTimeout(function(){
    if ($('#alert').length > 0) {
        $('#alert').remove();
    }
}, 3000);

function sweetalerts(mTitle, mText, mIcon, mButtons){
    swal({title: mTitle,text:mText, icon: mIcon, button: false});   
}

function send_json_ajax(type, url, sData, funcSuccess){
    $.ajax({
        type: type,
        url: url,
        data: sData,
        success: funcSuccess,
        dataType: 'json',
        contentType: 'application/json',
    });
}

function addOnShoppingCart(snackId, snackName, snackImg){
    let listIngredients = [];
    let inputListIngredients = $(".ingredients_"+snackId);
    for (let ingredient = 0; ingredient < inputListIngredients.length; ingredient++) {
        let getIngredient = inputListIngredients[ingredient];
        listIngredients.push(getIngredient.value);
    }
    let data = JSON.stringify({'id':parseInt(snackId), 
        'ingredients': JSON.stringify(listIngredients),
        'snackName': snackName,
        'snackImg':snackImg});
    send_json_ajax("POST",  "/addtocart/", data, successAddCart)
}

function successAddCart(response){
    if(response){
        swal({title: "Sucesso",text:"Lanche adicionado ao carrinho!", icon: "success", button: true}).then((value) => {location.reload()}); 
    }else{
        sweetalerts("Ops!", "Falha ao adicionar lanche no carrinho!", "warning", false);
    }
}

function successAddCartPlusIngredient(response){
    if(response){
        swal({title: "Sucesso",text:"Lanche adicionado ao carrinho!", icon: "success", button: true}).then((value) => {window.location.href="/shoppingcar/"; }); 
    }else{
        sweetalerts("Ops!", "Falha ao adicionar lanche no carrinho!", "warning", false);
    }
}

function addSnackOnCar(){
    let ingredients = [];
    let snackImg = $('#input_img').val();
    let snackName = $('#input_name').val();
    let qtdLettuce = parseInt($('#input_0').val());
    let qtdBacon = parseInt($('#input_1').val());
    let qtdBurger = parseInt($('#input_2').val());
    let qtdEgg = parseInt($('#input_3').val());
    let qtdCheese = parseInt($('#input_4').val());
    let snackValue = $('#value').text();
    snackValue = snackValue.split("Valor R$: ");
    snackValue = parseFloat(snackValue[1]);
    let listIngredients = [qtdLettuce, qtdBacon, qtdBurger, qtdEgg, qtdCheese]
    if(listIngredients.every(hasValue)){
    sweetalerts("Ops!", 
                `Para adicionar ao carrinho é necessario 
                que o lanche tenha ao menos um ingrediente selecionado.`,
                "warning",
                "OK");
    }else{
        ingredients = createListIngredients(ingredients,qtdLettuce, "Alface");
        ingredients = createListIngredients(ingredients,qtdBacon, "Bacon");
        ingredients = createListIngredients(ingredients,qtdBurger, "Hambúrguer de carne");
        ingredients = createListIngredients(ingredients,qtdEgg, "Ovo");
        ingredients = createListIngredients(ingredients,qtdCheese, "Queijo");
        
        let data = JSON.stringify({'ingredients': JSON.stringify(ingredients),
            'snackName': snackName,
            'snackImg':snackImg});
        send_json_ajax("POST",  "/addtocart/", data, successAddCartPlusIngredient)
    }
    
}
function createListIngredients(ingredients, amountLoop, text){
    for (let ingredientIndex = 0; ingredientIndex < amountLoop; ingredientIndex++) {
        ingredients.push(text)
        
    }
    return ingredients;
}

function moreThanZero(priceOfIngredient){
    return priceOfIngredient > 0;

}

function sendForm(form){
    priceLettuce = parseFloat($('#input_1').val());
    priceBacon = parseFloat($('#input_2').val());
    priceBurger = parseFloat($('#input_3').val());
    priceEgg = parseFloat($('#input_4').val());
    priceCheese = parseFloat($('#input_5').val());
    listPrisces = [priceLettuce, priceBacon, priceBurger, priceEgg, priceCheese];
    if(!listPrisces.every(moreThanZero)){
        sweetalerts("Ops!", "Ingredientes não podem ter o valor igual a 0, por favor verifique os valores!", "error", false)
    }else{
        $('#'+form).submit();
    }

}