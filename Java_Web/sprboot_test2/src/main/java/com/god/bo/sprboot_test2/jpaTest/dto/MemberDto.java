package com.god.bo.sprboot_test2.jpaTest.dto;

import lombok.Builder;

import javax.persistence.*;

@Entity(name="member")          // entity가 붙은 클래스는 JPA가 관리하는 클래스
public class MemberDto {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)       // 기본키 생성을 DB에 위임하기 위함. DB에서 auto increment를 사용하기에
    private Long mbrNo;
    private String id;
    private String name;

    public Long getMbrNo() {
        return mbrNo;
    }

    public void setMbrNo(Long mbrNo) {
        this.mbrNo = mbrNo;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MemberDto() {

    }

    @Builder
    public MemberDto(String id, String name){
        this.id = id;
        this.name = name;
    }


}
