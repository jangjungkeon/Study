<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="http://code.jquery.com/ui/1.8.18/jquery-ui.min.js"></script>
<link rel="stylesheet" type="text/css" href="http://code.jquery.com/ui/1.8.18/themes/base/jquery-ui.css"  />
<link rel="stylesheet" href="resources/css/signup.css">
<link rel="stylesheet" href="resources/css/dropdown.css">
<link rel="stylesheet" href="resources/css/top.css">
<script type="text/javascript">
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
	$(function(){
		$("#datepicker").datepicker({}); 
	});
		
		$("#submitBtn").click(
			function() {
				if ($("#user_id").val() === ""
						|| $("#user_pwd").val() === ""
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
    <jsp:include page="top.jsp"/>
    <div class="main">
      <div class="field_head">
        <h3 class="tit">회원가입</h3>
        <p class="sub"><span class="ico">*</span>필수입력사항</p>
      </div>

      <form action="signup" method="post" name="form">
        <table>
          <tr>
            <th>아이디<span class="ico">*</span></th>
            <td>
              <input
                type="text"
                name="user_id"
                id="user_id"
                placeholder="아이디를 입력하세요"
              />
            </td>
          </tr>
          <tr>
            <th>비밀번호<span class="ico">*</span></th>
            <td>
              <input
                type="password"
                name="user_pwd"
                id="user_pwd"
                maxlength="15"
                placeholder="비밀번호를 입력하세요(15자리 이하)"
              />
            </td>
          </tr>
          <tr>
            <th>이름<span class="ico">*</span></th>
            <td>
              <input
                type="text"
                name="user_name"
                id="user_name"
                placeholder="이름을 입력하세요"
              />
            </td>
          </tr>
          <tr>
            <th>이메일주소<span class="ico">*</span></th>
            <td>
              <input
                type="text"
                name="user_email"
                id="user_email"
                placeholder="이메일 주소를 입력하세요"
              />
            </td>
          </tr>
          <tr>
            <th>주소<span class="ico">*</span></th>
            <td>
              <input
                type="text"
                name="user_addr"
                id="user_addr"
                placeholder="주소를 입력하세요"
              />
            </td>
          </tr>
          <tr>
            <th>전화번호<span class="ico">*</span></th>
            <td>
              <input
                type="tel"
                name="user_tel"
                placeholder="숫자만 입력해주세요"
                pattern="[0-9]{2,3}-[0-9]{3,4}-[0-9]{3,4}"
                maxlength="13"
              />
            </td>
          </tr>
          <tr>
            <th id="gender">성별</th>
            <td>
              <input type="radio" name="user_gen" value="1" /> 남자
              <input type="radio" name="user_gen" value="0" /> 여자
              <input type="radio" name="user_gen" value="2" checked="checked" />
              선택안함
            </td>
          </tr>
          <tr>
            <th>생년월일</th>
            <td>
              <input type="text" id="datepicker" name="user_bDate" />
            </td>
          </tr>
        </table>
        <div id="submit">
          <input type="button" id="submitBtn" value="가입하기" />
        </div>
      </form>
    </div>
    <jsp:include page="bottom.jsp"/>
</body>
</html>









