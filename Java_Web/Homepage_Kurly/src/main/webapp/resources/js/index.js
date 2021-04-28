$(document).on('ready',function() {
	// 상품 넣고 ajax 처리.
	$.ajax({
		type : "get",
		url : "goodsRandom",
		dataType : "json",
		data : {"num" : 25},
		success : function(goodsList) {
			//alert(goodsList.datas);
			let list = goodsList.datas;
			$(list).each(function(idx, dto) {
				// alert(idx); 0 ~ 17
				idx++;
				let img = "resources/images/goods/"+ dto["goods_img"];
				let resultPrice = Number(dto["goods_price"])* (100 - Number(dto["goods_discountRate"]))/ 100;
				let link = "goods?goods_id="+ dto["goods_id"];resultPrice += "원";

				$("#index_a"+ idx).attr("href",link);
				$("#index_image"+ idx).attr("src",img);
				$("#index_goods_name"+ idx).text(dto["goods_name"]);
				$("#index_goods_Bprice" + idx).text(dto["goods_price"]+ "원");
				$("#index_goods_Pprice" + idx).text(resultPrice);});
		},
		error : function() {}
	});

	$(".regular").slick({
		dots : false,
		infinite : true,
		slidesToShow : 4,
		slidesToScroll : 1
	});

	$(".regular2").slick({
		dots : true,
		infinite : true,
		slidesToShow : 3,
		slidesToScroll : 1
	});

});