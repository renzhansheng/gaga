# TFwork说明

## Python版本与依赖库

- Python 3.6.6（SetupTools、pip）
- Httprunner 1.5.10
- selenium 2.53.1(3.11.0)   
- PyYaml
- xlrd
- xlwt
- requests
- JMESPath
- Faker

## TFwork目录说明

- TFwork(TFwork测试目录)
    - config(配置文件)
    - data(测试数据)
    - docs(文档)
    - img(图片)
    - drivers(驱动)
    - log(日志)
    - public(公共方法)
    - report(测试报表)
    - test(测试文件)
    	- case（测试用例）
        - case（api测试用例）
        - common（跟项目、页面无关的封装）
        - mock(模拟数据)
        - page（页面）
    	- Run_Tests.py(执行测试)
    - test_sps(httprunner)
        - data(测试数据)       
        - download (下载文件)
        - reports（测试报告）
        - testcases（测试用例）
        - debugtalk.py(httprunner共有方法)      
        - locustfile.py(执行性能测试) 
        - Run_Tests.py(执行测试) 