package com.god.bo.sprboot_test2.test.controller;

import com.god.bo.sprboot_test2.test.model.TestDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;


@Controller
public class TestController {
    private final Logger logger = LoggerFactory.getLogger(this.getClass());

    @RequestMapping(value="/testLogger")
    public ModelAndView test() throws Exception{
        logger.trace("Trace level 테스트");
        logger.debug("debug level 테스트");
        logger.info("info level 테스트");
        logger.warn("warn level 테스트");
        logger.error("error level 테스트");

        return new ModelAndView("test");
    }

    @RequestMapping(value="/home")
    public String home(){
        return "index.html";
    }

    // view 가 아닌 Data를 받고 싶다면 @ResponseBody. String, Map, Json 등의 객체를 받을 수 있음.
    @ResponseBody
    @RequestMapping("/valueTest")
    public String valueTest(){
        String value = "테스트 String";
        return value;
    }

    @RequestMapping("/thymeleafTest")
    public String thymeleafTest(Model model){
        TestDto testModel = new TestDto("jk", "장중건");
        model.addAttribute("testModel", testModel);
        return "thymeleaf/thymeleafTest";
    }

}
