package com.god.bo.sprboot_test2.test.mybatis;

import com.god.bo.sprboot_test2.test.model.JikwonDto;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface TestMapper {

    List<JikwonDto> selectTest();

}
