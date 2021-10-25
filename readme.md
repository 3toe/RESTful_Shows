Objectives:

    Practice ORM queries from the controller
    Practice RESTful routing
    Practice rendering query results to templates
    Practice using form input to create table data
    Using all 4 main CRUD commands

Update #1:
 - Added validations

 - In the editshow.html template, fix the release date field value from:
<input class="entry" type="date" name="reldate" value="{{show.reldate}}"">
to
<input class="entry" type="date" name="reldate" value="{{show.reldate|date:'Y-m-d'}}"">
adding the Django filter to allow the date to populate