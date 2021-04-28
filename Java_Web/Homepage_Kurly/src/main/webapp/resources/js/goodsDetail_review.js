

    /* 페이지 변경 */
    $(document).on('click', '.pagebtn', function page(){
        var pageId = this.id;
        var howAsc = $("#howAsc").val();
        var RorQ = $('.pagebtn').parent().attr('name');
        callReview(pageId, howAsc, RorQ);
    });

    /* 리뷰 정렬하기 */
    $(document).on('change', '#howAsc', function asc(){
        var pageId = 1;
        var howAsc = $("#howAsc").val();
        callReview(pageId, howAsc, "review");
    });

    /* 좋아요 버튼 클릭 */
    $(document).on('click', '.like_btn',function(){
        var review_id = this.id;
        $.ajax({
            type : "get",
            url : "clickLikes",
            data : {"review_id" : review_id},
            dataType : "json",
            success : function(data) {
                let result = data.result;
                let howAsc = data.howAsc;
                let pageId = data.page;
                if(result === "fail")
                    alert("로그인 후 이용해 주세요.")
                else if(result === "like"){
                    alert("추천해 주셔서 감사합니다.")
                    callReview(pageId, howAsc, "review");
                }else{
                    alert("추천이 취소되었습니다.")
                    callReview(pageId, howAsc, "review");
                }
            },
            error : function(){
                alert("오류발생");
            }
        });

    });

    /* 페이지 로딩될 때 1 페이지 표시됨 */
    $(function(){
        var pageId = 1;
        callReview(pageId, "recently" ,"review");
        callReview(pageId, "recently" ,"qna");

        var log = getParameterByName("log")
        if(log === "x"){
            alert("로그인 후 이용해주세요")
        }else{
        }

    });