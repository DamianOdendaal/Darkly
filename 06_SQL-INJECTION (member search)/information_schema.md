<h1>Using information schema</h1>

<h3> Microsoft SQL Server provides an information schema view as one of several methods for obtaining this metadata. As their support documentation states, “Information schema views provide an internal, system table-independent view of the SQL Server metadata ”</h3>

<h3>Simple way to get all tables that exist on a SQL server</h3>
<h3>
'''
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
'''
</h3>


<h1>::Some more notes::</h1>
<h3>In MySQL there is a lot of data that can be accessed inside the information_schema object like tables for example, the table information_schema.tables contains all the metadata related to table objects.</h3>

<h3>Some things we can get from the information schema object</h3>
<ul>

<li>table_name: The name of the table.</li>
<li>column_name: The name of the column.</li>
<li>data_type: Specifies the data type (MySQL data type).</li>
<li>column_default: Default value inserted in the column.</li>
<li>is_nullable: Indicates whether the column can contain null or not.</li>
</ul>

A great place to learn more about information schema is [here](https://dev.mysql.com/doc/refman/8.0/en/information-schema.html)