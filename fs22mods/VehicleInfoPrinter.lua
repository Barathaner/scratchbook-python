VehicleInfoPrinter = {};
VehicleInfoPrinter.modDirectory = g_currentModDirectory;
VehicleInfoPrinter.isLoaded = false;
local http = require("socket.http")
function VehicleInfoPrinter:loadMap(name)
    if self.isLoaded then
        return;
    end
    self.isLoaded = true;
    print("[VehicleInfoPrinter] Mod geladen.");
end;

function VehicleInfoPrinter:deleteMap()
    self.isLoaded = false;
end;

function VehicleInfoPrinter:update(dt)
    -- Ein Tastendruck zum Aktivieren (z.B. linke Alt + V)
    if InputBinding.isPressed(InputBinding.VEHICLE_EXTRA_FUNCTION1) and InputBinding.isPressed(InputBinding.VEHICLE_HORN) then
        self:printVehicleData();
    end
end;
function VehicleInfoPrinter:printVehicleData()
    local dataToSend = {}
    for _, vehicle in pairs(g_currentMission.vehicles) do
        local vehicleData = {
            name = vehicle.name,
            fillUnits = {}
        }
        if vehicle.getFillUnits ~= nil then
            for index, fillUnit in pairs(vehicle:getFillUnits()) do
                local fillTypeName = g_fillTypeManager:getFillTypeNameByIndex(fillUnit.fillType)
                table.insert(vehicleData.fillUnits, {
                    fillType = fillTypeName,
                    fillLevel = fillUnit.fillLevel
                })
            end
        end
        table.insert(dataToSend, vehicleData)
    end

    local jsonData = json.encode(dataToSend)
    local response, code = http.request("http://your_django_server/route", jsonData)
    if code ~= 200 then
        print("Fehler beim Senden der Daten: " .. response)
    end
end

addModEventListener(VehicleInfoPrinter);