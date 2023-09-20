VehicleInfoPrinter = {}
VehicleInfoPrinter.modDirectory = g_currentModDirectory

function VehicleInfoPrinter:loadMap(name)
    self.xmlFile = self.modDirectory .. "VehicleInfoPrinter.xml"
    self.lastUpdateTime = 0
end

function VehicleInfoPrinter:update(dt)
    -- Überprüfe, ob seit dem letzten Update 500ms vergangen sind
    if g_currentMission.time - self.lastUpdateTime >= 500 then
        local xmlContent = "<?xml version='1.0' encoding='UTF-8'?>\n<VehicleInfoPrinter>\n"

        if g_currentMission.controlledVehicle ~= nil then
            local fullName = g_currentMission.controlledVehicle:getFullName()
            local price = g_currentMission.controlledVehicle:getPrice()
            local lastSpeed = g_currentMission.controlledVehicle:getLastSpeed(true)

            xmlContent = xmlContent .. "<controlledVehicle>\n"
            xmlContent = xmlContent .. string.format("\t<fullName>%s</fullName>\n", fullName)
            xmlContent = xmlContent .. string.format("\t<price>%s</price>\n", price)
            xmlContent = xmlContent .. string.format("\t<lastSpeed>%s</lastSpeed>\n", lastSpeed)
            xmlContent = xmlContent .. "</controlledVehicle>\n"
        end

        local posX, posY, posZ, graphrot = g_currentMission.player:getPositionData()
        xmlContent = xmlContent .. string.format("<playerPosition x='%s' y='%s' z='%s' rotation='%s' />\n", posX, posY, posZ, graphrot)

        xmlContent = xmlContent .. "</VehicleInfoPrinter>"

        -- Speichern der generierten XML-Inhalte in der XML-Datei
        self.xmlFile = self.modDirectory .. "VehicleInfoPrinter.xml"
        local file = io.open(self.xmlFile, "w")
        file:write(xmlContent)
        file:close()

        -- Aktualisiere die lastUpdateTime Variable
        self.lastUpdateTime = g_currentMission.time
    end
end

addModEventListener(VehicleInfoPrinter)
