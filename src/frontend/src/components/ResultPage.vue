<template>
    <div>
      <div class="container">
        <div class="result-wrapper">
            <div class="input-section">
            <h1>Submitted Results</h1>
            <ul>
                <!-- show user inputs -->
                <li><b>Gender:</b> <span>{{ results.gender }}</span></li>
                <li><b>Age:</b> <span>{{ results.age }}</span></li>
                <li><b>Blood Pressure (Systolic / Diastolic):</b> <span>{{ results.bpSys }} / {{ results.bpDia }}</span></li>
                <li><b>Heart Disease:</b> <span>{{ results.heartDisease }}</span></li>
                <li><b>Smoking History:</b> <span>{{ results.smokeHistory }}</span></li>
                <li><b>Height:</b> <span>{{ results.height }} cm</span></li>
                <li><b>Weight:</b> <span>{{ results.weight }} kg</span></li>
                <li><b>Last Blood Sugar Level:</b> <span>{{ results.bloodSugar || 'Not provided' }}</span></li>
            </ul>
            </div>
            <div class="advice-section">
            <!-- show personalised advice  -->
            <h1>Advice based on results</h1>
            <p><b>Your BMI:</b> <span>{{ bmi }}</span></p>
            <p><b>Category:</b> <span>{{ bmiCategory }}</span></p>
            <p><b>Blood Pressure Advice:</b> <span :style="{ color: bpAdvice.color }">{{ bpAdvice.text }}</span></p>
            <p><b>Smoking History Advice:</b> <span :style="{ color: smokeAdvice.color }">{{ smokeAdvice.text }}</span></p>
            <p><b>BMI Advice:</b> <span :style="{ color: bmiAdvice.color }">{{ bmiAdvice.text }}</span></p>
            <p><b>Blood Sugar Advice:</b> <span :style="{ color: bloodSugarAdvice.color }">{{ bloodSugarAdvice.text }}</span></p>
            </div>
        </div>
        <!-- button for returning to questionnaire -->
        <div class="return-to-survey">
            <input type="button" value="Return To Questionnaire" @click="returnToQuestionnaire">
        </div>
      </div>
    </div>
  </template>
  
  <script>
  //import ref, computed and onMounted from vue, computed(defines computed properties, automatically updated if data changes)
  //onMounted(set up data and html beforehand, so it displays immediately after component is loaded)
  import { ref, computed, onMounted } from 'vue';
  //import useRouter
  import { useRouter } from 'vue-router';
  
  export default {
    //component name
    name: 'ResultsPage',
    setup() {
      //initailse array to empty values
      const results = ref({
        gender: '',
        age: '',
        bpSys: '',
        bpDia: '',
        heartDisease: '',
        smokeHistory: '',
        height: '',
        weight: '',
        bloodSugar: ''
      });
      
      //function for calculating bmi
      const bmi = computed(() => {
        const heightInMeters = results.value.height / 100;
        //return bmi to 2 decimal places
        return (results.value.weight / (heightInMeters ** 2)).toFixed(2);
      });
  
      //function returning bmi category
      const bmiCategory = computed(() => {
        const bmiValue = parseFloat(bmi.value);
        if (bmiValue < 18.5) return 'Underweight';
        if (bmiValue >= 18.5 && bmiValue <= 24.9) return 'Normal Weight';
        if (bmiValue > 24.9 && bmiValue <= 29.9) return 'Overweight';
        return 'Obese';
      });
      
      //function which returns advice base on blood pressure
      const bpAdvice = computed(() => {
        if (parseInt(results.value.bpSys) > 130 || parseInt(results.value.bpDia) > 80) {
          return { text: 'Your blood pressure is high. Consider reducing salt intake, staying active, and consulting your healthcare provider.', color: '#f44336' };
        }
        return { text: 'Your blood pressure is within a normal range. Keep up the healthy habits to maintain it.', color: '#4CAF50' };
      });
  
      //function which returns advice base on smoking history
      const smokeAdvice = computed(() => {
        const adviceMap = {
          'no info': { text: 'Smoking history information is not available.', color: '#777' },
          'never': { text: 'Great job avoiding smoking! Keep it up.', color: '#4CAF50' },
          'former': { text: 'It\'s great that you quit smoking!', color: '#4CAF50' },
          'current': { text: 'Smoking is harmful. Consider quitting for better health.', color: '#f44336' },
          'not current': { text: 'You\'ve stopped smoking! Stay smoke-free for long-term health.', color: '#4CAF50' },
          'ever': { text: 'Having smoked in the past means increased health risks. Stay smoke-free.', color: '#f44336' }
        };
        return adviceMap[results.value.smokeHistory.toLowerCase()] || { text: 'Invalid smoking history.', color: '#f44336' };
      });
  
      //function which returns advice base on bmi values
      const bmiAdvice = computed(() => {
        const bmiValue = parseFloat(bmi.value);
        if (bmiValue < 18.5) return { text: 'You are underweight. Consult a nutritionist.', color: '#f44336' };
        if (bmiValue >= 18.5 && bmiValue <= 24.9) return { text: 'Your weight is normal. Maintain a balanced diet.', color: '#4CAF50' };
        if (bmiValue > 24.9 && bmiValue <= 29.9) return { text: 'You are overweight. Consider healthier eating and activity.', color: '#f44336' };
        return { text: 'You are obese. Consider dietary and exercise changes.', color: '#f44336' };
      });
  
      //function which returns advice base on bloodglucose level
      const bloodSugarAdvice = computed(() => {
        const bloodSugar = parseInt(results.value.bloodSugar);
        if (bloodSugar < 70) return { text: 'Your blood sugar is low. Consider small meals and consult a healthcare provider.', color: '#f44336' };
        if (bloodSugar > 126) return { text: 'Your blood sugar is high. Consult a doctor to manage your blood sugar.', color: '#f44336' };
        return { text: 'Your blood sugar is normal. Maintain a balanced diet.', color: '#4CAF50' };
      });
  
      //function which retrieves user inputs
      const loadResults = () => {
        //parse the query string into URLSearchParam object 
        const urlParams = new URLSearchParams(window.location.search);
        //gets the user input values 
        results.value = {
          gender: urlParams.get('gender'),
          age: urlParams.get('age'),
          bpSys: urlParams.get('bp_sys'),
          bpDia: urlParams.get('bp_dia'),
          heartDisease: urlParams.get('heartdisease'),
          smokeHistory: urlParams.get('smokehis'),
          height: parseFloat(urlParams.get('height')),
          weight: parseFloat(urlParams.get('weight')),
          bloodSugar: urlParams.get('bloodsugar')
        };
      };
      
      //get results ready 
      onMounted(loadResults);

      const router = useRouter();
      //function to return to questionnaire page
      const returnToQuestionnaire = () => {
        router.push({name:'QuestionnairePage'});
      };
  
      //returns setup variables for template use
      return {
        results,
        bmi,
        bmiCategory,
        bpAdvice,
        smokeAdvice,
        bmiAdvice,
        bloodSugarAdvice,
        returnToQuestionnaire
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
  
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 20px;
    margin: 40px;
  }
  
  .input-section, .advice-section {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    padding: 20px;
    width: 45%;
    transition: all 0.3s ease;
  }
  
  .input-section h1, .advice-section h1 {
    color: #4CAF50;
    text-align: center;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  li {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .advice-section p {
    font-size: 1em;
    color: hsl(187, 31%, 27%);
    padding: 10px 0;
    border-bottom: 1px solid #ddd;
  }
  
  .advice-section span {
    font-weight: normal;
    color: #4CAF50;
  }

  .result-wrapper {
  display: flex;
  justify-content: center;
  gap: 20px;
  width: 100%;
}

.return-to-survey {
  margin-top: 20px; 
  text-align: center;
  width: 100%; 
}

.return-to-survey input[type="button"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-family: 'Raleway', sans-serif;
  }
  </style>
  