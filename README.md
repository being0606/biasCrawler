# biasCrawler
in AI ethics class, Web crawl + FaceDection = CREDIT



First, complete the job.csv file. This is the name of the query to be searched in the Google Image Search window. In my case, I put about 50 jobs in English-Korean, but it doesn't matter if it's not a job if it's something to search for.

| English             | Korean       |
|---------------------|--------------|
| Software Developer  | 소프트웨어 개발자 |
| Data Scientist      | 데이터 과학자  |
| Mechanical Engineer | 기계 공학자   |
| Civil Engineer      | 토목 엔지니어  |
| Electrical Engineer | 전기 엔지니어  |
| Nurse               | 간호사       |
| Doctor              | 의사         |
| Pharmacist          | 약사         |
| Dentist             | 치과 의사     |



After that, the initial screen (job_JOBNAME_img00.png) searched in each directory and the first to 20th pictures (job_JOBNAME_img00.png ~ job_JOBNAME_img20.png) are added to each directory as a png file.

<p align="center">
  <img src="DATA/screenshot/Accountant/job_Accountant_img00.png" alt="job_Accountant_img00.png">
  <img src="/DATA/screenshot/Accountant/job_Accountant_img01.png" alt="job_Accountant_img01.png" width="200">
  <img src="/DATA/screenshot/Accountant/job_Accountant_img02.png" alt="job_Accountant_img02.png" width="200">
</p>

After that, the race and gender of the extracted face image for each photo are analyzed using the Deepface model.

Make the analysis result back to the csv file.