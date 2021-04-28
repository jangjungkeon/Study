<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>마켓컬리 :: 내일의 장보기, 마켓컬리</title>
<script type="text/javascript" src="resources/js/jquery-3.5.1.min.js"></script>
<link href="resources/css/slick.css" rel="stylesheet" type="text/css" />
<link href="resources/css/slick-theme.css" rel="stylesheet" type="text/css" />
<link href="resources/css/index.css" rel="stylesheet" />
<link href="resources/css/slider.css" rel="stylesheet" />

<link href="resources/css/multipleImageSlider.css" rel="stylesheet" />
<link href="resources/css/earlyBirdContainer.css" rel="stylesheet" />
<link href="resources/css/dropdown.css" rel="stylesheet" />
<link rel="shortcut icon" href="resources/images/kurlyTop.png" />


</head>
<body>
	<div id="container">
		<jsp:include page="WEB-INF/views/top.jsp"/>

		<div class="main">
			<div class="carousel-container">
				<div class="carousel-slide">
					<img src="resources/images/mainSlider3.PNG" id="lastClone" />
					<img src="resources/images/mainSlider1.PNG" />
					<img src="resources/images/mainSlider2.PNG" />
					<img src="resources/images/mainSlider3.PNG" />
					<img src="resources/images/mainSlider1.PNG" id="firstClone" />
				</div>
				<button id="prevBtn"></button>
				<button id="nextBtn"></button>
			</div>

			<div class="howAbout">
				<h2 class="how">이 상품 어때요?</h2>
				<section class="regular slider">
					<% for (int i=1; i <= 6; i++) {
						String a_id = "index_a" + i;
						String img_id = "index_image" + i;
						String gname_id = "index_goods_name" + i;
						String gprice_id = "index_goods_Bprice" + i;
						String gpriceOrign_id = "index_goods_Pprice" + i;
					%>
						<div>
						<a id= <%= a_id %> href="#"><img id=<%= img_id %>
						src="http://placehold.it/250x320?text=1" /></a>
						<div id=<%= gname_id %>>상품명</div>
						<del id=<%= gprice_id %>>원래가격 : </del>
						<br/>
						<div id=<%= gpriceOrign_id %>>가격</div>
					</div>
					<%
					}
				%>
				</section>
				<br /> <br /> <br />
			</div>

			<div class="earlyBirdContainer">
				<div class="earlyBirdText">
					<br/><strong>설 얼리버드 특가</strong><br/><br/>ㅡ<br/><br/>
					<br/><span>설날까지 매일 진행되는 24시간 한정 특가</span><br/><br/><br />
					⏰ 망설이면 늦어요!<br/>
				</div>
				<div class="earlyBirdPic">
					<% for (int i=25; i == 25; i++) {
						String a_id = "index_a" + i;
						String img_id = "index_image" + i;
						String gname_id = "index_goods_name" + i;
						String gprice_id = "index_goods_Bprice" + i;
						String gpriceOrign_id = "index_goods_Pprice" + i;
					%>
					<a id= <%= a_id %> href="#"><img id=<%= img_id %> src="http://placehold.it/600x400?text=1" /></a>
					<div id=<%= gname_id %>>상품명</div>
					<del id=<%= gprice_id %>>원래가격 : </del>
					<br/>
					<div id=<%= gpriceOrign_id %>>가격</div>
					<%
						}
					%>

				</div>
				<br/><br/><br/><br />
			</div>

			<div class="eventNews" style="background-color: #f2f2f2">
				<br /> <br />
				<h2>이벤트 소식 ></h2>
				<section class="regular2 slider">
					<% for (int i=7; i <= 12; i++) {
						String a_id = "index_a" + i;
						String img_id = "index_image" + i;
						String gname_id = "index_goods_name" + i;
						String gprice_id = "index_goods_Bprice" + i;
						String gpriceOrign_id = "index_goods_Pprice" + i;
					%>
					<div>
						<a id= <%= a_id %> href="#"><img id=<%= img_id %>
																 src="http://placehold.it/250x320?text=1" /></a>
						<div id=<%= gname_id %>>상품명</div>
						<del id=<%= gprice_id %>>원래가격 : </del>
						<br/>
						<div id=<%= gpriceOrign_id %>>가격</div>
					</div>
					<%
						}
					%>
				</section>
				<br /> <br /> <br />
			</div>

			<div class="AlttlProducet">
				<br /> <br />
				<h2>알뜰 상품</h2>
				<section class="regular slider">
					<% for (int i=13; i <= 18; i++) {
						String a_id = "index_a" + i;
						String img_id = "index_image" + i;
						String gname_id = "index_goods_name" + i;
						String gprice_id = "index_goods_Bprice" + i;
						String gpriceOrign_id = "index_goods_Pprice" + i;
					%>
					<div>
						<a id= <%= a_id %> href="#"><img id=<%= img_id %>
																 src="http://placehold.it/250x320?text=1" /></a>
						<div id=<%= gname_id %>>상품명</div>
						<del id=<%= gprice_id %>>원래가격 : </del>
						<br/>
						<div id=<%= gpriceOrign_id %>>가격</div>
					</div>
					<%
						}
					%>
				</section>
				<br /> <br /> <br />
			</div>

			<div class="newProduct">
				<h2>오늘의 신상품 ></h2>
				<section class="regular slider">
					<% for (int i=19; i <= 24; i++) {
						String a_id = "index_a" + i;
						String img_id = "index_image" + i;
						String gname_id = "index_goods_name" + i;
						String gprice_id = "index_goods_Bprice" + i;
						String gpriceOrign_id = "index_goods_Pprice" + i;
					%>
					<div>
						<a id= <%= a_id %> href="#"><img id=<%= img_id %>
																 src="http://placehold.it/250x320?text=1" /></a>
						<div id=<%= gname_id %>>상품명</div>
						<del id=<%= gprice_id %>>원래가격 : </del>
						<br/>
						<div id=<%= gpriceOrign_id %>>가격</div>
					</div>
					<%
						}
					%>
				</section>
				<br /> <br /> <br />
			</div>
		</div>


		<jsp:include page="WEB-INF/views/bottom.jsp"/>
		<script type="text/javascript"
			src="//code.jquery.com/jquery-1.11.0.min.js"></script>
		<script type="text/javascript"
			src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
		<script type="text/javascript" src="resources/js/slick.min.js"></script>
		<script src="resources/js/slider.js"></script>
		<script src="resources/js/index.js"></script>
	</div>
</body>
</html>