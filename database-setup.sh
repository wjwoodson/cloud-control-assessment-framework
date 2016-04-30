sqlite3 ccaf.db '
CREATE TABLE framework(id integer primary key autoincrement, name text, description text);
CREATE TABLE provider(id integer primary key autoincrement, name text);
CREATE TABLE threat(id integer primary key autoincrement, framework_id integer, name text, description text, weight float, foreign key(framework_id) references framework(id));
CREATE TABLE control(id integer primary key autoincrement, framework_id integer, name text, description text, weight float, has_children bool, foreign key(framework_id) references framework(id));
CREATE TABLE assessment(id integer primary key autoincrement, framework_id integer, provider_id integer, name text, start_date datetime, end_date datetime, foreign key(framework_id) references framework(id), foreign key(provider_id) references provider(id));
CREATE TABLE rel_control(id integer primary key autoincrement, parent_control_id integer, child_control_id integer, foreign key(parent_control_id) references control(id), foreign key(child_control_id) references control(id));
CREATE TABLE rel_control_threat(id integer primary key autoincrement, threat_id integer, control_id integer, weight float, foreign key(threat_id) references threat(id), foreign key(control_id) references control(id));
CREATE TABLE control_test(id integer primary key autoincrement, provider_id integer, control_id integer, name text, type text, method text, description text, weight float, input_model blob, output_model blob, foreign key(provider_id) references provider(id), foreign key(control_id) references control(id));
CREATE TABLE control_test_result(id integer primary key autoincrement, control_test_id integer, assessment_id integer, success bool, score bool, date datetime, assessor text, output blob, foreign key(control_test_id) references control_test(id), foreign key(assessment_id) references assessment(id));'
