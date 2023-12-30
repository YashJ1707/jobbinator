package io.jobbinator_server.Rest;

import io.jobbinator_server.Entities.Job;
import io.jobbinator_server.Services.db_services.JobService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Objects;

@RestController
@RequestMapping("/jobs")
@CrossOrigin
public class RestJob {

    private JobService service;

    public RestJob(JobService service) {
        this.service = service;
    }

    @GetMapping("")
        public ResponseEntity<String> getJobs(@RequestParam(defaultValue = "empty") String website,  @RequestParam(defaultValue = "empty") String skill){
        List<Job> jobs;
            if(!Objects.equals(website, "empty")&&!Objects.equals(skill,"empty")){
                return service.getJobsForWebsiteAndSkill(website,skill);
            }else if(!Objects.equals(website, "empty")){
                return service.getJobsForWebsite(website);
            }else if(!Objects.equals(skill, "empty")){
                return service.getJobsForSkill(skill);
            }else{
                return service.getAllJobs();
            }
    }
}
