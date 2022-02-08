# Airflow

## Apache Airflow란?

Airflow는 워크 플로를 아래의 작업 수행하는 플랫폼이라고 설명할 수 있다.

- 코드로 작성하고
- 스케줄링한 뒤
- 모니터링

**Airflow의 장점**

- 과거 데이터 재처리 작업을 편리하게 수행



## Apache Airflow 기본 동작 원리

Airflow를 구성하는 각 컴포넌트와 역할, 실제 Airflow task가 어떠한 형태로 동작하는지 설명

![img](https://engineering.linecorp.com/wp-content/uploads/2021/01/k8sdataeng1.png)

- Scheduler : 가장 중추적 역할을 수행하며 모든 [DAG](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#dags)(Directed Acyclic Graph)와 태스크를 모니터링하고 관리합니다. 그리고 주기적으로 실행해야 할 태스크를 찾고 해당 태스크를 실행 가능한 상태로 변경합니다.
- Webserver : Airflow 웹 UI 서버입니다.
- Kerberos : 인증 처리를 위한 티켓 갱신(ticket renewer) 프로세스입니다(선택 사항).
- DAG Script : 개발자가 작성한 Python 워크 플로 스크립트입니다.
- MetaDB : Airflow 메타데이터 저장소입니다. 어떤 DAG가 존재하고 어떤 태스크로 구성되었는지, 어떤 태스크가 실행 중이고, 또 실행 가능한 상태인지 등의 많은 정보가 기입됩니다.
- Executor : 태스크 인스턴스를 실행하는 주체이며 종류가 다양합니다.
- Worker : 실제 작업을 수행하는 주체이며 워커의 동작 방식은 Executor의 종류에 따라 상이합니다.



- **HiveOperator를 예로 들어 간략히 설명**

![img](https://engineering.linecorp.com/wp-content/uploads/2021/01/k8sdataeng2-1024x463.png)

개발자가 HiveOperator에 실행하고 싶은 쿼리 입력 후, 태스크 작성시

내부적으로 Hive CLI명령어 생성

- 아래의 `_prepare_cli_cmd` 함수를 보면, 개발자가 정의한 DB호스트 정보, ID및 패스워드 정보와 함께 쿼리를 이용해 CLI 명령어 문자열을 구성하는 것을 확인할 수 있다.

**class HiveCliHook(BaseHook)**

```python
def _prepare_cli_cmd(self):
        conn = self.conn
        hive_bin = 'hive'
        cmd_extra = []

        if self.use_beeline:
            hive_bin = 'beeline'
            jdbc_url = "jdbc:hive2://{host}:{port}/{schema}".format(
                host=conn.host, port=conn.port, schema=conn.schema)
            if conf.get('core', 'security') == 'kerberos':
                template = conn.extra_dejson.get(
                    'principal', "hive/_HOST@EXAMPLE.COM")
                if "_HOST" in template:
                    template = utils.replace_hostname_pattern(
                        utils.get_components(template))

                proxy_user = self._get_proxy_user()

                jdbc_url += ";principal={template};{proxy_user}".format(
                    template=template, proxy_user=proxy_user)
            elif self.auth:
                jdbc_url += ";auth=" + self.auth

            jdbc_url = '"{}"'.format(jdbc_url)

            cmd_extra += ['-u', jdbc_url]
            if conn.login:
                cmd_extra += ['-n', conn.login]
            if conn.password:
                cmd_extra += ['-p', conn.password]

        hive_params_list = self.hive_cli_params.split()

        return [hive_bin] + cmd_extra + hive_params_list
```



이후에는 스케줄러는 Airflow 워커를 생성

- Airflow 워커는 Executor의 종류에 따라 동작 방식이 상이함

아래 코드는 LocalWoker 클래스에서 프로세스 형태로 워커가 실행되는 함수

- 파라미터로 전달받은 명령어는 airflow run으로 시작하는 명령어이며, Airflow 워커 실행 시 수행되는 명령어로 이해

**class LocalWorker (multiprocessing.Process, LoggingMixin)**

```python
def execute_work(self, key, command):
        if key is None:
            return
        self.log.info("%s running %s", self.__class__.__name__, command)
        try:
            subprocess.check_call(command, close_fds=True)
            state = State.SUCCESS
        except subprocess.CalledProcessError as e:
            state = State.FAILED
            self.log.error("Failed to execute task %s.", str(e))

        self.result_queue.put((key, state))
```

최종적으로 HiveOperator를 통해 만들어진 Hive명령어가 실행되고 Hive Java프로세스가 수행되는 원리



## Executor의 종류 및 특징과 장단점

Airflow에 Executor라는 개념이 있다.

**Executor**는 문자 그대로 작업의 한 단위인 **태스크 인스턴스를 실행하는 주체**

Executor에는 다양한 종류가 있고 각 종류에 따라 동작 원리가 상이하다.

- Debug Executor
- Local Executor
- Dask Executor
- Celery Executor
- Kubernetes Executor
- CeleryKubernetes Executor ( Airflow 2.0)



### Local Executor

![img](https://engineering.linecorp.com/wp-content/uploads/2021/01/k8sdataeng3-1024x490.png)

단일 장비에 웹 서버와 스케줄러를 같이 기동하고, 태스크를 프로세스 형태로 스폰(spawn)해 실행하는 형태

Airflow 워커는 

- 스케줄러가 서브 프로세스 형태로 실행하고 
- 해당 워커에서 실제 수행해야 하는 태스크를 실행

Local Executor는 `Parallelism`설정값에 따라 두 가지 구조로 나뉜다.

1. Unlimited Parallelism
   - 설정값이 0인 경우, 이론적으로 들어오는 모든 요청에 대해 무한대로 태스크 실행

2. Limited Parallelism
   - 설정값이 0 이상인 경우, 해당 설정값의 개수만큼 프로세스 수를 제한하여 태스크 실행

`task_queue`의 정보를 이용해 태스크 실행 수에 대한 스로틀링(throttling)을 한다.

Airflow워커의 구현체는 `QueuedLocalWorker`클래스이다.



**Local Executor 장점**

구성이 간단하다.

- 베타 혹은 테스트 환경에 많이 사용

환경을 빠르게 구성할 수 있다.

- 실 서비스 환경에 적용하는 사례도 있음

**Local Executor 단점**

SPOF(Single point of failure) 문제

- 단일 장비 환경에서의 작동이 원인

매번 프로세스 상태를 체크하며 모니터링해야 함

- 실제 서비스 환경에는 적합하지 않음



### Celery Executor

![img](https://engineering.linecorp.com/wp-content/uploads/2021/01/k8sdataeng4.jpg)

워커를 스케일아웃할 수 있는 방법 중 하나

Celery 백엔드로 메시지 브로커(broker)가 필요

- 메시지 브로커(broker)로는 RabbitMQ나 Redis사용

스케줄러는 실행해야 할 태스크를 메시지 브로커에 전달하고, 각 워커 장비의 Celery 워커가 태스크를 실행한다. 이때, 전달되는 태스크의 형태 명령어는 문자열



**Celery Executor 장점**

워커를 2대 이상 구성할 수 있다는 부분에서 SPOF 단점을 어느 정도 개선

- 서비스 환경에서 주로 사용

**Celery Executor 단점**

Master에 대한 SPOF단점은 그대로

- 이에 대한 프로세스 모니터링이 필요

메시지 브로커가 추가로 필요

- 관리 포인트가 늘어남