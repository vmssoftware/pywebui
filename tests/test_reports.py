def test_get_reports(connector):
    assert connector.get_reports()


def test_get_scripts(connector):
    assert connector.get_scripts()


def test_get_report(connector):
    report = connector.get_reports()[0]
    assert connector.get_report(report.fileName, report.directory)


def test_get_log(connector):
    report = connector.get_reports()[0]
    assert connector.get_log(report.fileName, report.directory)


def test_generate(connector):
    script = connector.get_scripts()[0]
    report = connector.get_reports()[0]
    assert connector.generate(
        script_dir=script.directory,
        script_name=script.fileName,
        report_dir=report.directory,
    )


def test_export_report(connector):
    report = connector.get_reports()[0]
    assert connector.export_report(report.fileName, report.directory)
