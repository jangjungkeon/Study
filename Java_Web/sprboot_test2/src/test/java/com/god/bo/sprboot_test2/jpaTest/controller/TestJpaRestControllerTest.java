package com.god.bo.sprboot_test2.jpaTest.controller;

import com.god.bo.sprboot_test2.jpaTest.dto.MemberDto;
import com.god.bo.sprboot_test2.jpaTest.service.MemberService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;
import org.springframework.web.filter.CharacterEncodingFilter;

import javax.transaction.Transactional;

import java.util.Optional;

import static org.assertj.core.api.BDDAssertions.then;
import static org.hamcrest.core.Is.is;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest(
        properties = {
                "testId=jkjk",
                "testName=장중건"
        }
        , webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT


)
@Transactional
@AutoConfigureMockMvc
@Slf4j
public class TestJpaRestControllerTest {

    @Value("${testId}")
    private String testId;

    @Value("${testName}")
    private String testName;

    @Autowired
    MockMvc mvc;

    @Autowired
    private TestRestTemplate restTemplate;

    // Service로 등록하는 빈
    @Autowired
    private MemberService memberService;

    @Autowired
    private WebApplicationContext ctx;

    @BeforeEach() //Junit4의 @Before
    public void setup() {
        this.mvc = MockMvcBuilders.webAppContextSetup(ctx).
                addFilters(new CharacterEncodingFilter("UTF-8", true))      // 필터 추가
                .alwaysDo(print())
                .build();
    }


    @Test
    void getMember() throws Exception {
        log.info("#### properties 테스트 #####");
        log.info("testId : " + testId);
        log.info("testName : " + testName);

        /******** START : MOC MVC test **********/
        log.info("******** START : MOC MVC test **********");
        mvc.perform(get("/memberTest/1")).
                andExpect(status().isOk()).
                andExpect(content().contentType(MediaType.APPLICATION_JSON)).
                andExpect(jsonPath("$.id", is("jkjk"))).
                andDo(print());
        log.info("******** END : MOC MVC test **********");
        /******** END : MOC MVC test **********/

        /******** START : TestRestTemplate test **********/
        log.info("******** START : TestRestTemplate test **********");
        ResponseEntity<MemberDto> response = restTemplate.getForEntity("/memberTest/1", MemberDto.class);
        then(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        then(response.getBody()).isNotNull();
        log.info("******** END : TestRestTemplate test **********");
        /******** END : TestRestTemplate test **********/


        /******** START : MockBean test **********/
        log.info("******** START : MockBean test **********");
        /* MemberDto memberDto = MemberDto.builder().
                                           id(testId).
                                           (testName).
                                           build();

        given(memberRepository.findById(1L)).
        willReturn(Optional.of(memberDto)); */


        Optional<MemberDto> member = memberService.findById(1L);
        if (member.isPresent()) {
            // Junit5 BDD 사용시
            then("jkjk").isEqualTo(member.get().getId());
            then("장중건").isEqualTo(member.get().getName());
        }
        log.info("******** END : MockBean test **********");
        /******** END : MockBean test **********/}
    }

