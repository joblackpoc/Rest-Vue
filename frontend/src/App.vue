<template>
  <div id="app">

    <form @submit.prevent="createStudent">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Fname" v-model="student.fname">
        <input type="text" class="form-control col-3 mx-2" placeholder="Lname" v-model="student.lname">
        <input type="text" class="form-control col-2 mx-2" placeholder="Course" v-model="student.course">
        <input type="text" class="form-control col-1 mx-2" placeholder="Rate" v-model="student.rating">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Fname</th>
        <th>Lname</th>
        <th>Course</th>
        <th>Rate</th>
        
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id">
          <td align="left">{{ student.fname }}</td>
          <td align="left">{{ student.lname }}</td>
          <td align="left">{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>


export default {
  name : 'App',
  data(){
    return {
      student:{
        'fname':'',
        'lname':'',
        'course':'',
        'rating':'',
      },
      students: []
    }
  },

  async created(){
    var response= await fetch('http://127.0.0.1:8000/api/student/')
    this.students = await response.json();
  },

  methods:{
    async createStudent(){
      var response= await fetch('http://127.0.0.1:8000/api/student/',{
        method:'post',
        headers:{
          'Content-Type':'application/json'
        },
        body: JSON.stringify(this.student)
      });
      this.students.push(await response.json());
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
