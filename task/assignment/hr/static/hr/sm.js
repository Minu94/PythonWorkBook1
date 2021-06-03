var URL="{% url 'unread' %}"
function MyFunction(){

    var x=document.getElementById("id_country").value;
    alert(x)
    var data = {
    country: x,
    };
    alert(data)
    $.post(URL, data);
    }
//csrfmiddlewaretoken: '{{ csrf_token }}'