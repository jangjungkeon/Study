package com.god.bo.sprboot_test2.test.controller;

import com.god.bo.sprboot_test2.test.model.JikwonDto;
import com.god.bo.sprboot_test2.test.model.TestDto;
import com.god.bo.sprboot_test2.test.service.TestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;

@Controller
public class JikwonController {

    @Autowired
    TestService testService;

    @RequestMapping(value="/jikwon")
    public ModelAndView test() throws Exception{
        ModelAndView mav = new ModelAndView("jikwon");

        List<JikwonDto> testList = testService.selectTest();
        for (JikwonDto dto : testList){
            System.out.println(dto.getJikwon_name());
        }

        mav.addObject("list", testList);

        return mav;
    }
}
