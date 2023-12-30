package io.jobbinator_server.Repositories;

import io.jobbinator_server.Entities.Job;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface JobRepository extends JpaRepository<Job,Long > {
    List<Job> findByWebsite(String email);

    List<Job> findByTagsContaining(String skill);

    List<Job> findByWebsiteAndTagsContaining(String website, String skill);
}
