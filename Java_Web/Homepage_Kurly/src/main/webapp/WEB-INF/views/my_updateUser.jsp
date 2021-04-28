<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="resources/js/jquery-3.5.1.min.js"></script>
<script src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css"
	href="http://code.jquery.com/ui/1.8.18/themes/base/jquery-ui.css" />
<link rel="stylesheet" href="resources/css/dropdown.css">
<link rel="stylesheet" href="resources/css/my_updateUser.css">
<link rel="stylesheet" href="resources/css/mypage.css">
<!-- <link rel="stylesheet" href="resources/css/my_showOrders.css">
 -->
<script>
jQuery.browser = {};
(function () {
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
 $(document).ready(function(){

	    var msg = "<%=request.getAttribute("msg1")%>"
				if (msg != "null") {
					alert(msg);
				}

				$(function() {
					$("#datepicker").datepicker({});
				});

				$("#submitBtn").click(
						function() {
							if ($("#user_pwd").val() === ""
									|| $("#user_pwd1").val() === ""
									|| $("#user_pwd2").val() === ""
									|| $("#user_name").val() === ""
									|| $("#user_email").val() === ""
									|| $("#user_addr").val() === ""
									|| $("#user_tel").val() === ""
									|| $("#datepicker").val() === "") {
								alert("필수 입력란이 비었습니다. 확인해주세요.");
								return false;
							}
							form.submit();
						})
			})
</script>

</head>
<body>
	<jsp:include page="top.jsp"/>
	<div class="mypage_wrapper">
	<div class="mypage">
		<h2 class="tit_snb">마이컬리</h2>
		<div class="inner_snb">
			<div class="mypage_list">
				<a href="showOrders">주문내역</a>
			</div>
			<div class="mypage_list">
				<a href="updateUser">개인정보 수정</a>
			</div>
		</div>
	</div>
	<div class="main">
		<div class="title">
			<h3 class="tit">개인 정보 수정</h3>
		</div>
		<p />

		<form action="updateUser" method="post" name="form">
			<table>
				<tr>
					<th>아이디<span class="ico">*</span></th>
					<td><input type="text" name="user_id"
						placeholder="${userInfo.user_id}" id="user_id" readonly="readonly"
						value="${userInfo.user_id}" class="textbox" /></td>
				</tr>
				<tr>
					<th>현재 비밀번호<span class="ico">*</span></th>
					<td><input type="password" name="user_pwd" id="user_pwd"
						maxlength="15" class="textbox" /></td>
				</tr>
				<tr>
					<th>새 비밀번호<span class="ico">*</span></th>
					<td><input type="password" name="user_pwd1" id="user_pwd1"
						maxlength="15" placeholder="비밀번호를 입력하세요(15자리 이하)" class="textbox" />
					</td>
				</tr>
				<tr>
				<tr>
					<th>새 비밀번호 확인<span class="ico">*</span></th>
					<td><input type="password" id="user_pwd2" id="user_pwd2"
						maxlength="15" placeholder="비밀번호를 입력하세요(15자리 이하)" class="textbox" />
					</td>
				</tr>
				<tr>
					<th>이름<span class="ico">*</span></th>
					<td><input type="text" name="user_name" id="user_name"
						value="${userInfo.user_id}" class="textbox" /></td>
				</tr>
				<tr>
					<th>이메일주소<span class="ico">*</span></th>
					<td><input type="text" name="user_email" id="user_email"
						value="${userInfo.user_email}" class="textbox" /></td>
				</tr>
				<tr>
					<th>주소<span class="ico">*</span></th>
					<td><input type="text" name="user_addr" id="user_addr"
						value="${userInfo.user_addr}" class="textbox" /></td>
				</tr>
				<tr>
					<th>전화번호<span class="ico">*</span></th>
					<td><input type="tel" name="user_tel" id="user_tel"
						value="${userInfo.user_tel}"
						pattern="[0-9]{2,3}-[0-9]{3,4}-[0-9]{3,4}" maxlength="13"
						class="textbox" /></td>
				</tr>
				<tr>
					<th id="gender">성별</th>
					<td><input type="radio" name="user_gen" value="1" /> 남자 <input
						type="radio" name="user_gen" value="0" /> 여자 <input type="radio"
						name="user_gen" value="2" checked="checked" /> 선택안함</td>
				</tr>
				<tr>
					<th>생년월일<span class="ico">*</span></th>
					<td><input type="text" id="datepicker" name="user_bDate"
						class="textbox" /></td>
				</tr>
			</table>
			<div id="submit">
				<input type="button" id="submitBtn" value="수정하기" />
			</div>
		</form>
	</div>
	</div>
	<jsp:include page="bottom.jsp"/>
</body>
</html>