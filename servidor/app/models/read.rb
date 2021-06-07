class Read < ApplicationRecord
  broadcasts_to ->(read) { :reads }
end
