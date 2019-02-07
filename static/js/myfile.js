
function productValue(){
    let qtdLetture = parseInt($('#input_0').val());
    let qtdBacon = parseInt($('#input_1').val());
    let qtdBurger = parseInt($('#input_2').val());
    let qtdEgg = parseInt($('#input_3').val());
    let qtdCheese = parseInt($('#input_4').val());
    total = (qtdLetture * 0.4) + (qtdBacon * 2) + (qtdBurger * 3) + (qtdEgg * 0.8) + (qtdCheese * 1.5);

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
function sendForm(){
    let qtdLetture = parseInt($('#input_0').val());
    let qtdBacon = parseInt($('#input_1').val());
    let qtdBurger = parseInt($('#input_2').val());
    let qtdEgg = parseInt($('#input_3').val());
    let qtdCheese = parseInt($('#input_4').val());
    let listIngredients = [qtdLetture, qtdBacon, qtdBurger, qtdEgg, qtdCheese]
    if(listIngredients.every(hasValue)){
        swal({
            title: "Ops!",
            text: "Para adicionar ao carrinho é necessario que o lanche tenha ao menos um ingrediente selecionado.",
            icon: "warning",
            button: "OK",
            });
    }else{
        $('#form-add-car').submit();
    }
}
function hasValue(currentValue){
    return currentValue == 0 
}