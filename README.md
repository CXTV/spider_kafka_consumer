# 基于Kafka的爬虫client配置
1. kafka地址配置

        .env
        {
            cafca_host: cafca_host,
            cafca_port: cafca_port
        }

2. mysql地址配置

        .env
        {
            db_host: db_host,   #host
            db_port: db_port,   #端口
            db_username: db_username,   #用户名
            db_password: db_password,   #密码
            db_database: db_database    #数据库
        }

3. 爬虫启动

        #财经日历
        python main.py -c Jin10calendar
        # python main.py -c Fx678calendar   #暂不启动，fx678和jin10每次只启动一个

        #文章
        python main.py -c Article

        #快讯
        python main.py -c Jin10kuaixun
        python main.py -c Fx678kuaixun
        python main.py -c Wallstreetcnkuaixun
