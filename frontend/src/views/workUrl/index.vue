<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="SIT环境">
        <el-row>
        <span></span>
        </el-row>
        <el-row>
            <a href="http://81.69.155.204/manager/" target="_blank"><el-button type="primary">运管后台（已迁至BOSS）</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://boss.sit.mcd.com.cn/portal/home" target="_blank"><el-button type="primary">BOSS</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://10.126.141.131:5600/app/kibana#/home?_g=()" target="_blank"><el-button type="primary">Kibana</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://81.69.166.125/pg/swagger-ui.html?wework_cfm_code=NRVUMiCGxMZvmbg%2BAQ9hWnw%2BqvXBf4o06k418hnf5r9Dhy83UOf298rDZPqhNPK3K25Vif23vpPyqZgFJ9k9RyBnpYoaFVOzOKMX%2B%2FSTYsMt#/middle-pay-controller/queryChannelUsingGET" target="_blank"><el-button type="primary">Swagger-middle</el-button></a>            
            <el-divider direction="vertical"></el-divider>
            <a href="http://crm.sit.mcd.com.cn/sentinel/console/#/dashboard" target="_blank"><el-button type="primary">Sentinel流控平台</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <el-button>+</el-button>
        </el-row>
      </el-form-item>
      

      <el-form-item label="UAT环境">
        <el-row>
        <span></span>
        </el-row>
        <el-row>
            <a href="http://175.24.155.185/manager" target="_blank"><el-button type="success">运管后台（已迁至BOSS）</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://boss.uat.mcd.com.cn/portal/home" target="_blank"><el-button type="success">BOSS</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://10.126.141.131:5600/app/kibana#/home?_g=()" target="_blank"><el-button type="success">Kibana</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://49.234.165.160/pg/swagger-ui.html?wework_cfm_code=NRVUMiCGxMZvmbg%2BAQ9hWnw%2BqvXBf4o06k418hnf5r9Dhy83UOf298rDZPqhNPK3K25Vif23vpPyqZgFJ9k9RyBnpYoaFVOzOKMX%2B%2FSTYsMt#/" target="_blank"><el-button type="success">Swagger-middle</el-button></a>            
            <el-divider direction="vertical"></el-divider>
            <a href="http://crm.uat.mcd.com.cn/sentinel/console/#/login" target="_blank"><el-button type="success">Sentinel流控平台</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <el-button>+</el-button>
        </el-row>
      </el-form-item>


      <el-form-item label="PT环境">
        <el-row>
        <span></span>
        </el-row>
        <el-row>
            <a href="http://42.192.176.176/manager/#/login" target="_blank"><el-button type="warning">运管后台（已迁至BOSS）</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://boss.pt.mcd.com.cn/portal/home" target="_blank"><el-button type="warning">BOSS</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://kibana-pt.mcdchina.org/app/home#/" target="_blank"><el-button type="warning">Kibana</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://81.69.156.103/pg/swagger-ui.html?wework_cfm_code=NRVUMiCGxMZvmbg%2BAQ9hWnw%2BqvXBf4o06k418hnf5r9Dhy83UOf298rDZPqhNPK3K25Vif23vpPyqZgFJ9k9RyBnpYoaFVOzOKMX%2B%2FSTYsMt#/middle-pay-controller/queryChannelUsingGET" target="_blank"><el-button type="warning">Swagger-middle</el-button></a>            
            <el-divider direction="vertical"></el-divider>
            <a href="http://crm.pt.mcd.com.cn/sentinel/console/#/login" target="_blank"><el-button type="warning">Sentinel流控平台</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <el-button>+</el-button>
        </el-row>
      </el-form-item>


      <el-form-item label="生产环境">
        <el-row>
        <span></span>
        </el-row>
        <el-row>
            <a href="https://payment.mcd.com.cn/manager" target="_blank"><el-button type="danger">运管后台（已迁至BOSS）</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://boss.mcdchina.net/portal/home" target="_blank"><el-button type="danger">BOSS</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://raven.mcdchina.org/logs/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-30m,to:now))&_a=(columns:!(_source),filters:!(),index:cb6c9480-786a-11ec-b54b-d97c6092f99a,interval:auto,query:(language:kuery,query:''),sort:!())" target="_blank"><el-button type="danger">Kibana</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://crm.mcd.com.cn/sentinel/console/#/dashboard" target="_blank"><el-button type="danger">Sentinel流控平台</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <el-button>+</el-button>
        </el-row>
      </el-form-item>


      <el-form-item label="TEST环境">
        <el-row>
        <span></span>
        </el-row>
        <el-row>
            <a href="http://150.158.215.122/manager/" target="_blank"><el-button type="info">运管后台（已迁至BOSS）</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://boss.test.mcd.com.cn/portal/home" target="_blank"><el-button type="info">BOSS</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://10.126.141.131:5600/app/kibana#/home?_g=()" target="_blank"><el-button type="info">Kibana</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://81.69.166.125/pg/swagger-ui.html?wework_cfm_code=NRVUMiCGxMZvmbg%2BAQ9hWnw%2BqvXBf4o06k418hnf5r9Dhy83UOf298rDZPqhNPK3K25Vif23vpPyqZgFJ9k9RyBnpYoaFVOzOKMX%2B%2FSTYsMt#/middle-pay-controller/queryChannelUsingGET" target="_blank"><el-button type="info">Swagger-middle</el-button></a>            
            <el-divider direction="vertical"></el-divider>
            <a href="http://crm.test.mcd.com.cn/sentinel/console/#/dashboard" target="_blank"><el-button type="info">Sentinel流控平台</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <el-button>+</el-button>
        </el-row>
      </el-form-item>
      

      <el-form-item label="通用地址">
        <el-row>
        <span></span>
        </el-row>
        <el-row>
            <a href="https://console.cloud.tencent.com/tke2/cluster?rid=4" target="_blank"><el-button type="primary">腾讯云集群管理</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://console.cloud.tencent.com/redis#/" target="_blank"><el-button type="primary">腾讯云redis管理</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://mone.ninja.mcdchina.net/deploy/deploylist" target="_blank"><el-button type="primary">发布计划列表</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://pmo.mcd.com.cn/jira/projects/PG?selectedItem=com.atlassian.jira.jira-projects-plugin%3Arelease-page&status=released-unreleased" target="_blank"><el-button type="primary">Payment发布版本</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://pmo.mcd.com.cn/confluence/pages/viewpage.action?pageId=41897353" target="_blank"><el-button type="primary">Payment迭代开发</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="http://42.192.18.128:17948/zone/55302430967988224/assets/scenes/1?size=10" target="_blank"><el-button type="primary">笨马压测平台</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://api-docs.mcd.com.cn/group/1417" target="_blank"><el-button type="primary">Yapi接口管理平台</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://rancher.devops.mcd.com.cn/g/clusters" target="_blank"><el-button type="primary">Rancher</el-button></a>
            <el-divider direction="vertical"></el-divider>
            <a href="https://pmo.mcd.com.cn/jira/secure/Tempo.jspa#/teams/team/10/timesheet/?columns=PORTION_OF_REQUIRED_COLUMN&dateDisplayType=days&from=2022-03-01&groupBy=worker&periodType=CURRENT_PERIOD&subPeriodType=MONTH&teamId=10&to=2022-03-31&viewType=TIMESHEET" target="_blank"><el-button type="primary">工时统计</el-button></a>
            <el-divider direction="vertical"></el-divider>
        </el-row>
        <el-row>
        <el-divider color></el-divider>
        </el-row>
        <el-row>
        <a href="https://raven.mcdchina.org/metrics/d/m1LgjGink/zhong-tai-da-ping-jian-kong?orgId=1&from=now-3h&to=now" target="_blank"><el-button type="primary">Grafana中台监控大屏</el-button></a>
        <el-divider direction="vertical"></el-divider>
        <a href="https://monitor.mcdchina.org/d/9dy7WTm7z/4-1-payment-online?orgId=1" target="_blank"><el-button type="primary">Online监控面板</el-button></a>
        <el-divider direction="vertical"></el-divider>
        <a href="https://monitor.mcdchina.org/d/ikSB9H9Gk/4-2-payment-offline?orgId=1" target="_blank"><el-button type="primary">Offline监控面板</el-button></a>
        <el-divider direction="vertical"></el-divider>
        <a href="https://archery.ninja.mcd.com.cn/dashboard/" target="_blank"><el-button type="primary">SQL查询平台</el-button></a>
        <el-divider direction="vertical"></el-divider>
        <el-button>+</el-button>
        </el-row>
      </el-form-item>

      
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      }
    }
  },
  methods: {
    onSubmit() {
      this.$message('submit!')
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    }
  }
}
</script>

<style scoped>
.line{
  text-align: center;
}
</style>

