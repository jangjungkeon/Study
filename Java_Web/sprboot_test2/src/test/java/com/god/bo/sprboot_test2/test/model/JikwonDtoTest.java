package com.god.bo.sprboot_test2.test.model;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class JikwonDtoTest {

    @Test
    void getJikwon_name() {
        final JikwonDto dto = new JikwonDto();
        dto.setJikwon_name("중건쨩");
        assertEquals("중건쨩", dto.getJikwon_name());
    }

    // 오류나는 테스트.
    @Test
    void test2() {
        final JikwonDto dto = new JikwonDto();
        dto.setJikwon_no("123");
        assertEquals("1234", dto.getJikwon_no());
    }

    // assertEquals(a, b) : 객체 A와 B의 실제 값이 일치한지 확인한다.
    // assertSame(a, b) : a,b 가 같은 객체인지 확인
    // assertTrue(a) : 조건 A가 참인가를 확인한다.
    // assertNotNull(a) : 객체 A가 null이 아님을 확인한다.

}