import unittest
import HtmlTestRunner  # HTML 리포트 생성 라이브러리

def run_all_tests():
    # TestLoader를 사용하여 테스트 파일 로드
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 'test_case_1.py'와 'test_case_2.py'를 테스트 스위트에 추가
    suite.addTests(loader.discover('Testcase', pattern='test_mainhome.py'))
    suite.addTests(loader.discover('Testcase', pattern='test_mypage.py'))

    # 결과 리포트 생성을 위한 HTMLTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(
        combine_reports=True, 
        open_in_browser=True,
        report_title="Test Report",
        add_timestamp=True  # 리포트 파일에 타임스탬프 추가
    )
    
    # 테스트 실행 및 HTML 리포트 생성
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
