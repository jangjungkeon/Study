$(document).on("click", "#checkAll", function() {
    if ($("input[name=goods_checkAll]:checkbox").prop("checked")) {
        $("input[name=goods_check]:checkbox").prop("checked", true);
    } else {
        $("input[name=goods_check]:checkbox").prop("checked", false);
    }
    calc();
});

// 체크시 금액 변동
$(document).on("click", ".goods_check", calc);

$(document).on('click', '.btn_clear', del);

$(document).on('click', '.btn_down', function() {
    let num = $(this).next().val();
    let goods_id = $(this).attr("id").split("_down")[0];
    if (num > 1) {
        $(this).next().val(--num);

        let afterPrice = $("#"+goods_id+"_price").text();
        afterPrice *= num / (num + 1);

        // 변경된 숫자 및 금액 반영
        $("#"+goods_id+"_price").text(afterPrice);

        calc();

        // 변경된 수량 ajax를 통해 db로 전달
        let user_id = $("#user_id").val();
        updateCart(user_id, goods_id, num)

    }

});

$(document).on('click', '#btn_order', function(){
    if(confirm("정말 주문하시겠습니까?")){
        myform.submit();
    } else {
        return false;
    }
})

$(document).on('click', '.btn_up', function() {
    let num = $(this).prev().val();
    let goods_id = $(this).attr("id").split("_up")[0];
    /* alert(num) */
    if (num < 1000) {
        $(this).prev().val(++num);

        let afterPrice = $("#"+goods_id+"_price").text();

        afterPrice *= num / (num - 1)

        // 변경된 숫자 및 금액 반영
        $("#"+goods_id+"_price").text(afterPrice);
        calc();

        // 변경된 수량 ajax를 통해 db로 전달
        let user_id = $("#user_id").val();
        updateCart(user_id, goods_id, num)

    }
});