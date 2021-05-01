package com.god.bo.sprboot_test2.jpaTest.controller;

import com.god.bo.sprboot_test2.jpaTest.dto.MemberDto;
import com.god.bo.sprboot_test2.jpaTest.service.MemberService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("memberTest")
public class TestJpaRestController {
    // 기본형
    private final Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    MemberService memberService;

    // 모든 회원 조회
    @GetMapping(produces = {MediaType.APPLICATION_JSON_VALUE})      // produces => 출력하고자하는 데이터 포맷을 정의.
    public ResponseEntity<List<MemberDto>> getAllmembers() {
        List<MemberDto> member = memberService.findAll();
        return new ResponseEntity<List<MemberDto>>(member, HttpStatus.OK);
    }

    // 회원번호로 한명의 회원 조회
    @GetMapping(value = "/{mbrNo}", produces = {MediaType.APPLICATION_JSON_VALUE})
    public ResponseEntity<MemberDto> getMember(@PathVariable("mbrNo") Long mbrNo) {
        Optional<MemberDto> member = memberService.findById(mbrNo);
        return new ResponseEntity<MemberDto>(member.get(), HttpStatus.OK);
    }


    // 회원번호로 회원 삭제
    @DeleteMapping(value = "/{mbrNo}", produces = {MediaType.APPLICATION_JSON_VALUE})
    public ResponseEntity<Void> deleteMember(@PathVariable("mbrNo") Long mbrNo) {
        memberService.deleteById(mbrNo);
        return new ResponseEntity<Void>(HttpStatus.NO_CONTENT);
    }

    // 회원번호로 회원 수정(mbrNo로 회원을 찾아 Member 객체의 id, name로 수정함)
    @PutMapping(value = "/{mbrNo}", produces = {MediaType.APPLICATION_JSON_VALUE})
    public ResponseEntity<MemberDto> updateMember(@PathVariable("mbrNo") Long mbrNo, MemberDto member) {
        memberService.updateById(mbrNo, member);
        return new ResponseEntity<MemberDto>(member, HttpStatus.OK);
    }

    // 회원 입력
    @PostMapping
    public ResponseEntity<MemberDto> save(MemberDto member) {
        return new ResponseEntity<MemberDto>(memberService.save(member), HttpStatus.OK);
    }

    // 회원 입력
    @RequestMapping(value = "/saveMember", method = RequestMethod.GET)
    public ResponseEntity<MemberDto> save(HttpServletRequest req, MemberDto member) {
        return new ResponseEntity<MemberDto>(memberService.save(member), HttpStatus.OK);
    }

}
