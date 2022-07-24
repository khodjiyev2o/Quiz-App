// creating an array and passing the number, questions, options, and answers



 


      
var url = 'http://127.0.0.1:8000/api/questions';
     const everything = async function getData(){
        const response = await fetch(url);
        const data = await response.json();
        
        var arr = []
        const questionss = data.map((question) => {
          
          return {
            numb: question.id,
            question: question.question,
            answer : '',
            options: [],
             
            
          
          }
          });
          
          for(i=0;i<data.length;i++){
            var arr=[]
            data[i].options.map((values)=>{
              
              if(values.correct==true){
                questionss[i].answer = values.option
              }
              questionss[i].options.push(values.option)
             
              return arr
            })
           
            
          }
          
         
          return questionss
        };
       
     

everything().then((res)=>
  console.log(res)
);


let questions = [
    {
    numb: 1,
    question: "Is Samandar single or taken? ",
    answer: "Single",
    options: [
      "Single",
      "Taken",
      "Married",
      "Do not know"
    ]
  },
    {
      numb: 2,
    question: "What is Samandar's favorite color?",
    answer: "Blue",
    options: [
      "Red",
      "Blue",
      "Black",
      "White"
    ]
  },
    {
      numb: 3,
    question: "Samandar has never ever...",
    answer: "Dropped his/her cellphone in the toilet",
    options: [
      "Slept for 12 hours",
      "Broken a bone",
      "Dropped his/her cellphone in the toilet",
      "Ate a whole pizza by himself"
    ]
  },
    {
      numb: 4,
    question: "Who is Samandar's favorite, Mom or Dad?",
    answer: "Both",
    options: [
      "Mom",
      "Dad",
      "Both",
      "Do not know"
    ]
  },
    {
      numb: 5,
    question: "How many schools has Samandar gone to?",
    answer: "1",
    options: [
      "1",
      "2",
      "3",
      "4"
    ]
  },
  // you can uncomment the below codes and make duplicate as more as you want to add question
  // but remember you need to give the numb value serialize like 1,2,3,5,6,7,8,9.....

     {
    numb: 6,
    question: " How old is Samandar?",
    answer: "18",
    options: [
     "17",
    "18",
    "19",
    "20"
     ]
   },
];

console.log(questions)
