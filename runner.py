import os
import shutil
import subprocess
import webbrowser
from datetime import datetime

def execute_features():
    """
    Method helps to run the feature files and generate the BDD report using Allure
    :return:
    """
    current_directory = os.getcwd()

    # Ensure paths exist before use
    allure_results_path = os.path.join(current_directory, 'reports', 'allure-results')
    allure_report_path = os.path.join(current_directory, 'reports', 'allure-report')
    failure_screenshots_path = os.path.join(current_directory, 'failure_screenshots')

    # Remove existing directories and their contents
    if os.path.exists(allure_results_path):
        shutil.rmtree(allure_results_path)
    if os.path.exists(allure_report_path):
        shutil.rmtree(allure_report_path)
    if os.path.exists(failure_screenshots_path):
        shutil.rmtree(failure_screenshots_path)

    os.makedirs(allure_results_path, exist_ok=True)  # Create if it doesn't exist
    os.makedirs(allure_report_path, exist_ok=True)  # Create if it doesn't exist

    #Run tests with allure as the reporter
    command = ["behave", "-f","allure_behave.formatter:AllureFormatter", "-o", allure_results_path, "-f", "pretty"]
    subprocess.run(command, check=True)
    print("\nTest cases are executed successfully. The results will be available at " + allure_results_path)

    # Generate Allure report HTML
    generate_command = ["allure", "generate", "--single-file", "--clean", allure_results_path, "-o", allure_report_path]
    subprocess.run(generate_command, check=True)
    print("\nAllure report has been generated. Open the report at " + allure_report_path)

    #Open allure report
    allure_report_url = os.path.join(allure_report_path, 'index.html')
    webbrowser.open(allure_report_url, new=2)
    print("\nAllure report has been generated and opened. You can view the report in your web browser.")

if __name__ == '__main__':
    execute_features()
