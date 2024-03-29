<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="http://code.jquery.com/ui/1.8.18/themes/base/jquery-ui.css" />
<link rel="stylesheet" href="resources/css/admin.css">
<script>
	jQuery.browser = {};
	(function() {
		jQuery.browser.msie = false;
		jQuery.browser.version = 0;
		if (navigator.userAgent.match(/MSIE ([0-9]+)\./)) {
			jQuery.browser.msie = true;
			jQuery.browser.version = RegExp.$1;
		}
	})();
</script>
<script src="${pageContext.request.contextPath}/resources/js/datepicker.js"></script>
	<script type="text/javascript">
		$(document).ready(
				function() {
					$("#goods_saleBegin").datepicker({});
					$("#goods_saleEnd").datepicker({});

					$("#submitBtn").click(function() {
						form.submit();
					})
				})

	</script>
</head>
<body>
	<jsp:include page="top.jsp"/>
	<div class="main">
		<div id="test"></div>
		<div class="field_head">
			<h3 class="tit">ADMIN</h3>
			<!-- <p class="sub"><span class="ico">*</span>필수입력사항</p> -->
		</div>
		<form action="insertGoods" method="post" name="form" enctype="multipart/form-data">
			<table>
				<tr>
					<th>상품명</th>
					<td><input type="text" name="goods_name" /></td>
				</tr>
				<tr>
					<th>카테고리</th>
					<td><select id="category_id" name="category_id">
							<c:forEach var="i" items="${categoryList}">
								<option value="${i.category_id}">${i.category_name}</option>
							</c:forEach>
					</select></td>
				</tr>
				<tr>
					<th>짧은설명</th>
					<td><input type="text" name="goods_shortDesc" /></td>
				</tr>
				<tr>
					<th>상세정보</th>
					<td><textarea rows="10" cols="50" name="goods_detail"></textarea>
					</td>
				</tr>
				<tr>
					<th>원가</th>
					<td><input type="number" name="goods_price" /></td>
				</tr>
				<tr>
					<th>판매시작일</th>
					<td><input type="text" id="goods_saleBegin"
						name="goods_saleBegin" /></td>
				</tr>
				<tr>
					<th>판매종료일</th>
					<td><input type="text" id="goods_saleEnd" name="goods_saleEnd" />
					</td>
				</tr>
				<tr>
					<th>배송방법</th>
					<td><input type="text" name="goods_delivery" /></td>
				</tr>

				<tr>
					<th>등록자</th>
					<td><input type="text" name="goods_reg" /></td>
				</tr>
				<tr>
					<th>포장타입</th>
					<td><select name="goods_state">
							<option>냉장</option>
							<option>냉동</option>
							<option>상온</option>
					</select></td>
				</tr>
				<tr>
					<th>업로드할 이미지</th>
					<td><input type="file" id="fileImg" name="fileImg" size="200">
						<%@ taglib prefix="form"
							uri="http://www.springframework.org/tags/form"%>
						<form:errors path="file" cssStyle="color:red" />
						<p /> <input type="hidden" id="goods_img" name="goods_img"></td>
				</tr>
				<tr>
					<th>할인률</th>
					<td><input type="number" name="goods_discountRate" /></td>
				</tr>
				<tr>
					<th>판매단위</th>
					<td><input type="text" name="goods_saleUnit" /></td>
				</tr>
				<tr>
					<th>중량</th>
					<td><input type="text" name="goods_weight" /></td>
				</tr>
				<tr>
					<th>유통기한</th>
					<td><input type="text" name="goods_shelfLife" /></td>
				</tr>
				<tr>
					<th>알레르기 정보</th>
					<td><input type="text" name="goods_allergy" /></td>
				</tr>
				<tr>
					<th>안내사항</th>
					<td><input type="text" name="goods_info" /></td>
				</tr>
			</table>
			<div id="submit">
				<input type="button" value="등록" id="submitBtn" />
				<c:if test="${Msg != null }">
					<b style="color: blue"></b>
				</c:if>
			</div>
		</form>
	</div>
	<jsp:include page="bottom.jsp"/>
</body>
</html>