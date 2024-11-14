<template>
    <div>
        <!-- header for title -->
      <h1 style="text-align: center;">Diabetes Prediction Questionnaire</h1>

      <!-- form -->
      <form @submit.prevent="handleSubmit" id="questionnaireForm" :class="{ 'fade-out': isSubmitting }">

        <!-- loop through fields -->
        <div v-for="(field, index) in fields" :key="index" class="field-section" :class="{ active: index === currentFieldIndex }">
          <label :for="field.id"><b>{{ field.label }}</b></label>
          
          <!-- input template for each of the questions, if field type matches, the tempalte will be chosen for the question -->
          <template v-if="field.type === 'select'">
            <select :id="field.id" v-model="formData[field.model]" required>
              <option value="" disabled>Select Here</option>
              <!-- loop through option and generate a drop down list -->
              <option v-for="option in field.options" :key="option" :value="option">{{ option }}</option>
            </select>
          </template>
  
          <template v-else-if="field.type === 'text' || field.type === 'number'">
            <input :type="field.type" :id="field.id" :placeholder="field.placeholder" v-model="formData[field.model]" :min="field.min" :max="field.max" :step="field.step" required />
          </template>
  
          <template v-else-if="field.type === 'flex-inputs'">
            <div class="flex-inputs">
              <input type="number" id="bp_sys" placeholder="Systolic" v-model="formData.bp_sys" min="80" max="200" required>
              <input type="number" id="bp_dia" placeholder="Diastolic" v-model="formData.bp_dia" min="40" max="120" required>
            </div>
          </template>
          <!-- buttons  -->
          <div class="navigation-buttons">
            <input v-if="index > 0" type="button" value="Back" @click="previousField">
            <input v-if="index < fields.length - 1" type="button" value="Next" @click="nextField">
            <input v-if="index === fields.length - 1" type="submit" value="Submit">
          </div>
        </div>
      </form>
      <!-- show error message if any -->
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  //import Vue's ref function for creating reactive variables(ref listens for changes and automatically updates the web-page)
  import { ref } from 'vue';
  //import useRouter from vue-router for navigation between web page
  import { useRouter } from 'vue-router';
  
  export default {
    //component name
    name: 'QuestionnairePage',
    setup() {
      //declare and initialise reactive variable
      const currentFieldIndex = ref(0);
      const isSubmitting = ref(false);
      const errorMessage = ref('');
      const router = useRouter();
  
      //initialise array with empty values
      const formData = ref({
        gender: '',
        age: '',
        bp_sys: '',
        bp_dia: '',
        heartDisease: '',
        smokeHistory: '',
        height: '',
        weight: '',
        bloodSugar: ''
      });
      //initialise array which contains the form options and structure
      const fields = ref([
        { id: 'gender', label: 'Gender:', type: 'select', model: 'gender', options: ['Male', 'Female', 'Prefer Not To Say'] },
        { id: 'age', label: 'Age:', type: 'number', model: 'age', min: 1, max: 120 },
        { id: 'bloodpressure', label: 'Blood Pressure (Systolic / Diastolic):', type: 'flex-inputs', model: 'bp' },
        { id: 'heartdisease', label: 'Do you currently have heart disease?', type: 'select', model: 'heartDisease', options: ['Yes', 'No'] },
        { id: 'smokehis', label: 'Do you have a smoking history?', type: 'select', model: 'smokeHistory', options: ['No Info', 'Never', 'Former', 'Current', 'Not Current', 'Ever'] },
        { id: 'height', label: 'Height(cm):', type: 'number', model: 'height', min: 1 },
        { id: 'weight', label: 'Weight(kg):', type: 'number', model: 'weight', min: 1, step: 0.1 },
        { id: 'bloodsugar', label: 'Last Blood Sugar Level:', type: 'text', model: 'bloodSugar', placeholder: 'Enter blood sugar level' }
      ]);
      
      //Function Next button
      const nextField = () => {
        //only if there's an input it will procedd
        if (validateField()) {
          //increment the index
          if (currentFieldIndex.value < fields.value.length - 1) {
            currentFieldIndex.value++;
          }
        }
      };

      //Function Back button
      const previousField = () => {
        //only if the it's current index is > 0
        if (currentFieldIndex.value > 0) {
          //decrement index
          currentFieldIndex.value--;
        }
      };
      
      //Function for checking if an option was chosen
      const validateField = () => {
        //gets the current field
        const currentField = fields.value[currentFieldIndex.value];
        //gets input from formData
        const value = formData.value[currentField.model];
        //if there's no input, it will alert the user for an input and returns as false
        if (value === '') {
          alert(`${currentField.label} is required.`);
          return false;
        }
        //otherwise if there's an input it will return true
        return true;
      };
      //Function to handle submission 
      const handleSubmit = () => {
        //set isSubmitting to tru
        isSubmitting = true;
        //directs to ResultPage
          router.push({
                name: 'ResultPage',
                //sends formData to ResultPage
                query: formData.value 
            });
        };
    
      //returns variables from setup, so template could use the variables
      return {
        currentFieldIndex,
        isSubmitting,
        errorMessage,
        formData,
        fields,
        nextField,
        previousField,
        handleSubmit
      };
    }
  };
  </script>
  
  <style scoped>
  body {
    font-family: 'Raleway', sans-serif;
    background-color: #f4f4f9;
    color: #333;
    margin: 0;
    padding: 0;
  }
  
  h1 {
    color: #4CAF50;
  }
  
  form {
    background: white;
    max-width: 600px;
    margin: auto;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: opacity 0.8s ease;
  }
  
  .fade-out {
    opacity: 0;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 5px;
    display: block;
  }
  
  input[type="text"], input[type="number"], select {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
  }
  
  .flex-inputs {
    display: flex;
    gap: 10px;
  }
  
  .navigation-buttons {
    display: flex;
    justify-content: space-between;
    gap: 10px;
  }
  
  input[type="button"], input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-family: 'Raleway', sans-serif;
  }
  
  .field-section {
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transition: max-height 0.8s ease, opacity 0.8s ease;
  }
  
  .field-section.active {
    max-height: 500px;
    opacity: 1;
    transition: max-height 0.8s ease, opacity 0.8s ease;
  }
  
  .first-field .navigation-buttons {
    justify-content: flex-end;
  }
  </style>
  