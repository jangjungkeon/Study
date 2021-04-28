function del(){
    if (confirm("정말 삭제하시겠습니까?") === true){
        let a = $(this).parent()
        let user_id = $("#user_id").val();

        let goods_id = $(this).attr('value');

        $.ajax({
            type : "get",
            url : "deleteCartGoods",
            dataType : "json",
            data : {
                "goods_id" : goods_id,
                "user_id" : user_id
            },
            success : function(item) {
                if (item.isSuccess) {
                    a.remove();
                } else {
                    alert("해당 상품을 삭제할 수 없습니다")
                }
            }
        })
    } else {
        return false;
    }
}

function calc() {
    let mychklist = $("input[name=goods_check]:checkbox")
    let countArr = $(".inp")
    let priceArr = $(".goods_price")

    let totalPrice = 0;
    let discountprice = 0
    let totalDisPrice = 0
    let price = 0;
    //화면에 출력된 전체 상품목록에서 체크된 상품의 가격과 수량을 곱해서 금액 구하고 totalPrice에 누적
    $("input[name=goods_check]:checkbox").each(function(idx, mychklist) {
        let num = $(".inp")[idx].value;
        let rate = $(".goods_discountRate")[idx].value;
        let goods_price = $(".goods_price")[idx].value;

        if (mychklist.checked) {
            discountprice -= goods_price * num * (rate) / 100
            totalPrice += goods_price * num;
            totalDisPrice += goods_price * num * (100 - rate) / 100;
        }
    });

    $(".goodsPrice").text(totalPrice);
    $("#goodsPrice").val(totalPrice);
    $(".discountprice").text(discountprice);
    $("#discountprice").val(discountprice);
    $(".orders_price").text(totalDisPrice);
    $("#orders_price").val(totalDisPrice);
}

function updateCart(user_id, goods_id, num){
    $.ajax({
        type : "get",
        url : "updateCartGoods",
        dataType :"json",
        data : {"goods_id":goods_id, "user_id":user_id, "cart_goods_cont":num},
        success:function(item){
            if (!item.isSuccess) {
                alert("해당 상품의 구매갯수를 변경할 수 없습니다.")
            }
        }
    })
}