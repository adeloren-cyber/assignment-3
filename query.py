import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS
    print(f"ALL TESTS")
    cursor.execute('SELECT project_name, actual_strength, passed FROM concrete_tests')
    while row := cursor.fetchone():
        project_name = row['project_name']
        actual_strength = row['actual_strength']
        passed = row['passed']
        print(f"{project_name} : {actual_strength} PSI - {passed}")
    


    # 2. Show ONLY failed tests
    print(f"FAILED TESTS")
    cursor.execute('SELECT project_name, test_date, required_strength, actual_strength FROM concrete_tests WHERE passed=0')
    while row:= cursor.fetchone():
            project_name = row['project_name']
            test_date = row['test_date']
            required_strength = row['required_strength']
            actual_strength = row['actual_strength']
            print(f"{project_name} on {test_date}")
            print(f"Required: {required_strength} PSI")
            print(f"Actual: {actual_strength} PSI")

    # 3. Count tests by project
    print(f"TEST PER PROJECT")
    cursor.execute('SELECT project_name, COUNT(*) FROM concrete_tests GROUP BY project_name')
    while row:= cursor.fetchone():
          project_count = row['COUNT(*)']

    cursor.execute('SELECT project_name, COUNT(*) FROM concrete_tests WHERE passed = 1 GROUP BY project_name ORDER BY project_name ASC')
    while row:= cursor.fetchone():
            project_name = row['project_name']
            project_count_passed = row['COUNT(*)']
            print(f"{project_name}: {project_count_passed}/{project_count} passed")