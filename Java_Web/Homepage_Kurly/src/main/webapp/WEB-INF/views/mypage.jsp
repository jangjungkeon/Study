<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="resources/js/jquery-3.5.1.min.js"></script>
</head>
<body>
<jsp:include page="top.jsp"/>
** 마이페이지 **
 <div id="btn_user"><a href="updateUser"> 개인정보 수정 </a></div>
 <div id="btn_orders"><a href="showOrders"> 주문 내역 </a></div><br> 
 <jsp:include page="bottom.jsp"/>
</body>
</html>