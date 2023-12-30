package io.jobbinator_server.Services.db_services;

import com.google.gson.Gson;
import io.jobbinator_server.Entities.Job;
import io.jobbinator_server.Repositories.JobRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class JobService {

    private final JobRepository repository;
    Gson gson=new Gson();
    public JobService(JobRepository repository) {
        this.repository = repository;
    }

    public ResponseEntity<String> getAllJobs(){
        List<Job> jobs=repository.findAll();
        System.out.println(jobs.size());
        String json=gson.toJson(jobs);
        return ResponseEntity.ok().body(json);
    }

    public ResponseEntity<String> getJobsForWebsite(String website){
        List<Job> jobs=repository.findByWebsite(website);
        String json=gson.toJson(jobs);
        return ResponseEntity.ok().body(json);
    }

    public ResponseEntity<String> getJobsForSkill(String skill){
        List<Job> jobs=repository.findByTagsContaining(skill);
        String json=gson.toJson(jobs);
        return ResponseEntity.ok().body(json);
    }
    public ResponseEntity<String> getJobsForWebsiteAndSkill(String website, String skill){
        List<Job> jobs=repository.findByWebsiteAndTagsContaining(website,skill);
        String json=gson.toJson(jobs);
        return ResponseEntity.ok().body(json);
    }

}
