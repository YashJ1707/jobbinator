package io.jobbinator_server.Repositories;

import io.jobbinator_server.Entities.Company;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CompanyRepository extends JpaRepository<Company, Long> {

}
