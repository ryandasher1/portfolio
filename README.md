## Portfolio

A simple, static website for projects I've worked on.

### Commands

Activate virtual environment on Windows:

    .\virtualenvs\pelican\Scripts\activate

Build the content:

    pelican content

Copy the content to S3:

    aws s3 cp --recursive .\output\ $S3_BUCKET

