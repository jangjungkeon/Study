package com.god.bo.sprboot_test2.jpaTest.service;

import com.god.bo.sprboot_test2.jpaTest.dto.MemberDto;
import com.god.bo.sprboot_test2.jpaTest.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class MemberService {
    @Autowired
    private MemberRepository memberRepository;

    public List<MemberDto> findAll(){
        List<MemberDto> members = new ArrayList<MemberDto>();
        memberRepository.findAll().forEach(e -> members.add(e));
        return members;
    }

    public Optional<MemberDto> findById(Long mbrNo){
        Optional<MemberDto> member = memberRepository.findById(mbrNo);
        return member;
    }

    public void deleteById(Long mbrNo) {
        memberRepository.deleteById(mbrNo);
    }

    public MemberDto save(MemberDto member){
        memberRepository.save(member);
        return member;
    }

    public void updateById(Long mbrNo, MemberDto member){
        Optional<MemberDto> e = memberRepository.findById(mbrNo);

        if (e.isPresent()){
            e.get().setMbrNo(member.getMbrNo());
            e.get().setId(member.getId());
            e.get().setName(member.getName());
            memberRepository.save(member);
        }
    }
}
