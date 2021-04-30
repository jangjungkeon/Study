package com.god.bo.sprboot_test2.test.service;

import com.god.bo.sprboot_test2.test.model.JikwonDto;
import com.god.bo.sprboot_test2.test.mybatis.TestMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TestService {

    @Autowired
    public TestMapper mapper;

    public List<JikwonDto> selectTest(){
        return mapper.selectTest();
    }
}
