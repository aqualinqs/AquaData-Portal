-- Drop existing tables if any
DROP TABLE IF EXISTS business_links, file_manager, aquaculture_business, supplier, market, investor CASCADE;

-- Create tables 
-- 1. Businesses
CREATE TABLE aquaculture_business (
    id SERIAL PRIMARY KEY,
    business_name TEXT NOT NULL,
    owner_name TEXT NOT NULL,
    contact_email TEXT,
    contact_phone TEXT,
    region TEXT,
    district TEXT,
    gps_lat DECIMAL(9,6),
    gps_lon DECIMAL(9,6),
    business_type TEXT,
    fish_species TEXT[],
    production_capacity INT,
    certification TEXT[],
    challenges TEXT,
);

-- Seed businesses
INSERT INTO aquaculture_business (business_name, owner_name, contact_email, contact_phone, region, district, gps_lat, gps_lon, business_type, fish_species, production_capacity, certification, challenges)
VALUES 
('BlueFish Farms', 'Ama Mensah', 'ama@bluefish.com', '+233201234567', 'Greater Accra', 'Tema', 5.6500, -0.0165, 'Grow-out', ARRAY['Tilapia', 'Catfish'], 5000, ARRAY['FDA'], 'Lack of feed'),
('AquaGold Hatchery', 'Kojo Owusu', 'kojo@aquagold.com', '+233209876543', 'Ashanti', 'Kumasi', 6.6900, -1.6150, 'Hatchery', ARRAY['Tilapia'], 10000, ARRAY['MoFA'], 'High mortality');

-- 2. Suppliers
CREATE TABLE supplier (
    id SERIAL PRIMARY KEY,
    supplier_name TEXT NOT NULL,
    supply_type TEXT,
    products_supplied TEXT[],
    region TEXT,
    contact_email TEXT,
    contact_phone TEXT
);

INSERT INTO supplier (supplier_name, supply_type, products_supplied, region, contact_email, contact_phone)
VALUES
('FreshFeeds Ltd', 'Feed', ARRAY['Tilapia Feed', 'Catfish Feed'], 'Greater Accra', 'contact@freshfeeds.com', '+233204567890'),
('AquaTech Equip', 'Equipment', ARRAY['Tanks', 'Aerators'], 'Ashanti', 'info@aquatech.com', '+233207654321');

-- 3. Markets
CREATE TABLE market (
    id SERIAL PRIMARY KEY,
    marketer_name TEXT,
    buyer_type TEXT,
    region TEXT,
    fish_required TEXT[],
    volume_required INT,
    contact_email TEXT,
    contact_phone TEXT
);

INSERT INTO market (marketer_name, buyer_type, region, fish_required, volume_required, contact_email, contact_phone)
VALUES
('Makola Market', 'Retail', 'Greater Accra', ARRAY['Tilapia'], 2000, 'buy@makola.com', '+233208765432'),
('Sunyani Fish Depot', 'Wholesale', 'Bono', ARRAY['Catfish'], 5000, 'contact@sunyani.com', '+233202345678');

-- 4. Investors
CREATE TABLE investor (
    id SERIAL PRIMARY KEY,
    investor_name TEXT,
    investment_type TEXT,
    interest_area TEXT[],
    min_ticket_size INT,
    max_ticket_size INT,
    contact_email TEXT,
    contact_phone TEXT
);

INSERT INTO investor (investor_name, investment_type, interest_area, min_ticket_size, max_ticket_size, contact_email, contact_phone)
VALUES
('AgriImpact Fund', 'Equity', ARRAY['Feed Production', 'Women-led Farms'], 10000, 50000, 'info@agriimpact.org', '+233205556666'),
('FishFinance Ghana', 'Debt', ARRAY['Infrastructure', 'Cold Chain'], 5000, 30000, 'finance@fishghana.com', '+233203333444');

-- 5. Business links
CREATE TABLE business_links(
    id SERIAL PRIMARY KEY,
    business_id INT REFERENCES aquaculture_business(id),
    partner_id INT,
    partner_type TEXT CHECK (partner_type IN ('supplier', 'market', 'investor')),
    relationship_type TEXT CHECK (relationship_type IN ('current', 'potential'))
);

-- 6. File_manager
CREATE TABLE file_manager(
    id SERIAL PRIMARY KEY,
    business_id INT REFERENCES aquaculture_business(id),
    file_name TEXT,
    file_type TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- seed file manager
INSERT INTO file_manager (file_name, file_type, uploaded_at)
VALUES
('certificate.pdf', 'pdf', '00:01:03');