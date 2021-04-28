<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="resources/js/jquery-3.5.1.min.js"></script>
<link rel="stylesheet" href="resources/css/goodsList.css">
</head>
<body>
<jsp:include page="top.jsp"/>
    <main>
      <div id="content">
        <div class="page_article">
          <!-- <div id="menu">신상품</div> -->
          <div id="goodsList">
            <div class="list_goods">
              <div class="inner_listgoods">
                <ul class="list">
                  <c:forEach var="i" items="${list}"><li>
                    <div class="item">
                      <div class="thumb">
                        <a
                          href="goods?goods_id=${i.goods_id}"
                          class="img"
                          style="
                            background-image: url('https://img-cf.kurly.com/shop/data/goods/1611301749352l0.jpg');
                          "
                          ><!---->
                          <img
                            src="resources/images/goods/${i.goods_img}"
                            alt="${i.goods_id }"
                            width="308"
                            height="396"
                        /></a>
                      </div>
                      <div class="info">
                        <span class="name">
                          ${i.goods_name }
                        </span>
                        <span class="cost">
                          <span class="price">${i.goods_price}원</span>
                        </span>
                        <span class="desc">${i.goods_shortDesc }</span>
                        <span class="tag"></span>
                      </div>
                    </div>
                  </li>
                  </c:forEach>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
    <jsp:include page="bottom.jsp"/>

 
</body>
</html>