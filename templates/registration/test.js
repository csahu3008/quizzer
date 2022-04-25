$('#contributer').on('click',function(){
    var $inp6=$("<input>",{type:'button',id:'contributerbtn',class:'btn btn-success',value:'Contributer'})
      $('#forms-section').html("{{form.as_p|linebreaks}}").append($inp6)
      
   });