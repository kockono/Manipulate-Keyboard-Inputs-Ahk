keys = {
    "h1": "#",
    "h2": "##",
    "h3": "###",
    "h4": "####",
    "h5": "#####",
    "h6": "######",
    "Ω" : ">",
    "exportpcm": "export POSTGRESCONNECTIONSTRING='Host=10.19.5.100;Database=postgres;Username=postgres;Password=30083008;Pooling=false;Timeout=300;CommandTimeout=300'",
    "exportpce": "export POSTGRESCONNECTIONSTRING='Host=10.19.5.100;Database=postgres;Username=postgres;Password=30083008;Pooling=false;Timeout=300;CommandTimeout=300'",
    "exportraven": "RAVENDB_URL = \"http://10.19.5.41:8082/\"",
    "makemigration":"dotnet ef migrations add \"AddTable\" --startup-project ../Delta.Api",
    "updatemigration": "dotnet ef database update --startup-project ../Delta.api" 
}

special_keys = {
    "Shift+Z": "<",
}
