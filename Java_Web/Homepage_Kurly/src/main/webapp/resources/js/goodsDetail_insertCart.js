    function calPrice(num){
  		let dc_price = $(".dc_price").text();
  		$(".num").text(num * dc_price);
  	}

  	/* 구매 수량 변동 */
  	$(document).on('click', '.btn_down_on',function(){
  		let num = $(".inp").val();
  		if (num > 0) $(".inp").val(--num);
  		calPrice(num);

	  });
    $(document).on('click', '.btn_down_up',function(){
  		let num = $(".inp").val();
  		if (num < 1000) $(".inp").val(++num);
  		calPrice(num);
	  });
