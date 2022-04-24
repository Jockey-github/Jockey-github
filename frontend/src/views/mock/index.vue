<template>
  <div class="app-container">
    <el-row display="margin-top:10px">
      <el-input v-model="input_mockname" placeholder="请输入mock名" style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="addmock()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
      <el-table :data="list_mock" element-loading-text="Loading" border fit highlight-current-row>
        <el-table-column align="center" label="ID" width="95">
          <template slot-scope="scope">
            {{ scope.row.pk }}
          </template>
        </el-table-column>
        <el-table-column label="mock_name">
          <template slot-scope="scope">
            {{ scope.row.fields.mock_name }}
          </template>
        </el-table-column>
        <el-table-column label="Time" align="center">
          <template slot-scope="scope">
            <span>{{ scope.row.fields.add_time }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
  import {
    getList,
    addmock
  } from '@/api/mock'

  export default {
    filters: {
      statusFilter(status) {
        const statusMap = {
          published: 'success',
          draft: 'gray',
          deleted: 'danger'
        }
        return statusMap[status]
      }
    },
    data() {
      return {
        list_mock: null,
        listLoading: true,
        input_mockname: ''
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        this.listLoading = true
        getList().then(response => {
          if (response.error_num === 0) {
            this.list_mock = response['list']
            this.listLoading = false
          } else {
            this.$message.error('查询mock失败')
            console.log(response['msg'])
          }
        })
      },
      addmock() {
        addmock(this.input_mockname).then(response => {
          if (response.error_num === 0) {
            this.getList()
            this.input_mockname = ''
          } else {
            this.$message.error('新增mock失败，请重试')
            console.log(response['msg'])
          }
        })
      }
    }
  }
</script>