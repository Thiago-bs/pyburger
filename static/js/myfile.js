function promotions(listProducts){
    let priceLettuce = parseFloat($('#qtd_input_1').val())
    let priceBacon = parseFloat($('#qtd_input_2').val())
    let priceBurger = parseFloat($('#qtd_input_3').val())
    let priceEgg = parseFloat($('#qtd_input_4').val())
    let priceCheese = parseFloat($('#qtd_input_5').val())
    let total = 0;

    total = (listProducts[0] * priceLettuce) + (listProducts[1] * priceBacon) + (listProducts[2] * priceBurger) + (listProducts[3] *priceEgg) + (listProducts[4] * priceCheese);
    if(listProducts[0] > 0 && listProducts[1] == 0){
        total =   total - (total * 0.1 )  
    }
    if(listProducts[1] >= 3 || listProducts[2] >= 3 ){
        let qtdLessIngredientBacon = Math.floor(listProducts[1]/3);
        let qtdLessIngredienthamburguer = Math.floor(listProducts[2]/3);
        qtdLessIngredientBacon =  qtdLessIngredientBacon * priceBacon;
        qtdLessIngredienthamburguer = qtdLessIngredienthamburguer * priceBurger;
        total -= qtdLessIngredientBacon;
        total -= qtdLessIngredienthamburguer;
    }
    if(listProducts[4] >= 3){
        let qtdLessIngredientCheese = Math.floor(listProducts[4]/3);
        qtdLessIngredientCheese = qtdLessIngredientCheese * priceCheese;
        total -= qtdLessIngredientCheese;
    }

    return total 

}



function productValue(){
    let qtdLettuce = parseInt($('#input_0').val());
    let qtdBacon = parseInt($('#input_1').val());
    let qtdBurger = parseInt($('#input_2').val());
    let qtdEgg = parseInt($('#input_3').val());
    let qtdCheese = parseInt($('#input_4').val());
    let listProducts = [qtdLettuce, qtdBacon, qtdBurger, qtdEgg, qtdCheese]
    let total = promotions(listProducts)

    $('#value').text("Valor R$: " + total.toFixed(2).toString());
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
function sendForm(form){
    let qtdLettuce = parseInt($('#input_0').val());
    let qtdBacon = parseInt($('#input_1').val());
    let qtdBurger = parseInt($('#input_2').val());
    let qtdEgg = parseInt($('#input_3').val());
    let qtdCheese = parseInt($('#input_4').val());
    let listIngredients = [qtdLettuce, qtdBacon, qtdBurger, qtdEgg, qtdCheese]
    if(listIngredients.every(hasValue)){
        swal({
            title: "Ops!",
            text: "Para adicionar ao carrinho é necessario que o lanche tenha ao menos um ingrediente selecionado.",
            icon: "warning",
            button: "OK",
            });
    }else{
        $('#'+form).submit();
    }
}
function hasValue(currentValue){
    return currentValue == 0 
}

setTimeout(function(){
    if ($('#alert').length > 0) {
        $('#alert').remove();
    }
}, 3000)