<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<link rel="stylesheet"
	href="https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css">

<link rel="stylesheet" href="resources/css/cartList.css">
</head>
<body>
	<jsp:include page="top.jsp"/>
	<div class="main">
		<div class="title">
			<h1>장바구니</h1>
		</div>
		<input type="hidden" name="user_id" id="user_id" value="<%=session.getAttribute("user_id")%>"/>
		<form action="preOrders" name="myform" method="post">
			<div class="inner_check">
				<label class="check"><input type="checkbox"
					name="goods_checkAll" id="checkAll"><span class="ico"></span>전체선택</label>
			</div>

			<div class="box_wrapper">
				<div class="boxList">
					<c:forEach var="c_dto" items="${cartList}">
						<c:set var="goods" value="${c_dto.goods_id}" />
						<div class="box">
							<label class="check"><input type="checkbox"
								class="goods_check" id="${goods}" name="goods_check"
								value="${goods}" /><span class="ico"></span> </label><img width="100"
								width="100" src="resources/images/goods/${c_dto.goods_img}">
							<span class="goods_name">${c_dto.goods_name}</span> <span
								class="count"><button type="button" id="${goods}_down" class="btn_down">-</button><input type="text" name="goods_cont" id="${goods}_cont"
								readonly="readonly" onfocus="this.blur()" class="inp"
								value="${c_dto.cart_goods_cont}" size="4" style="text-align:center; width:30px;"><button type="button" id="${goods}_up" class="btn_up">+</button></span>

							<!-- span으로 묶음 -->
							<span class="price_sum"> <span class="goods_price_calc" id="${goods}_price"> ${c_dto.goods_price * c_dto.cart_goods_cont * (100 - c_dto.goods_discountRate)/100}</span><span>원</span></span> 
							<input type="hidden" name="goods_price" class="goods_price" value="${c_dto.goods_price}"> 
							<input type="hidden" name="goods_discountRate" class="goods_discountRate" value="${c_dto.goods_discountRate}">
							<button type="button" id="${goods}_clear" class="btn_clear" value="${c_dto.goods_id}"></button>
						</div>
					</c:forEach>
				</div>

				<div class="bill">
					<div class="amount_view">
						<div class="amount">
							<span class="tit">상품금액</span> <span class="goodsPrice"></span><span>원</span>
							<input type="hidden" name="goodsPrice" id="goodsPrice">
						</div>
						<div class="amount">
							<span class="tit">상품할인금액</span> <span class="discountprice"></span><span>원</span>
							<input type="hidden" name="discountprice" id="discountprice">
						</div>
						<div class="amount lst">
							<span class="tit">결제 예정 금액</span> <br> <span
								class="orders_price"></span><span id="won">원</span> <input
								type="hidden" name="orders_price" id="orders_price">
						</div>
					</div>
					<div class="btn_wrapper">
						<input type="submit" id="btn_order" value="구매하기">
					</div>
				</div>

			</div>

		</form>
	</div>

	<script src="${pageContext.request.contextPath}/resources/js/cartList_func.js"></script>
	<script src="${pageContext.request.contextPath}/resources/js/cartList_event.js"></script>



</body>
</html>