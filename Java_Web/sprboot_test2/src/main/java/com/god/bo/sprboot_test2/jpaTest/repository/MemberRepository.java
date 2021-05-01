package com.god.bo.sprboot_test2.jpaTest.repository;

import com.god.bo.sprboot_test2.jpaTest.dto.MemberDto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface MemberRepository extends JpaRepository<MemberDto, Long> {
    // findBy뒤에 컬럼명을 붙여주면 이를 이용한 검색이 가능하다

    public List<MemberDto> findById(String id);

    public List<MemberDto> findByName(String name);

    //like검색도 가능
    public List<MemberDto> findByNameLike(String keyword);

}
