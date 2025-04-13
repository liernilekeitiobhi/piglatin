
// translate-form ID-a duen elementuaren "submit" evento baten zain egongo da etengabe:
document.getElementById("translate-form").addEventListener("submit", async function(e) {
    
    e.preventDefault(); //errorea maneiatu (konbentzioz JS-n sartzen dena)

    // HTML-ko "phrase" ID duen elementuaren balioa aldagai batean sartu:
    const phrase = document.getElementById("phrase").value;

    // "/translate" URL-an POST metodoa erabiltzen dugu. Hau da gure backend-arekin konektatuko den zatia. (ikusi app.py URL honetan gertatzen dena ikusteko)
    const response = await fetch("/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phrase })
    });

    // aplikazioaren erantzuna json formatuan jasotzen dugu. await horren bidez, response osoa eduki arte itxaroten dugu. 
    const data = await response.json();

    // result ID duen HTML-ko zatian erantzunaren translation atributua eransten dugu.
    document.getElementById("result").textContent = "Pig Latin: " + data.translation;
  });